# -*- coding: utf-8 -*-
"""Build the notes catalogue  -- the index for the whole notes tree.

Usage:
    python make_catalogue.py                # rebuild the catalogue
    python make_catalogue.py --root <dir>   # use another notes root

What it does
------------
* walks the notes root (depth 3), finds every .md and .pdf
* reads the first '# ' heading of each .md as its title
* counts the images a note references (relative ./figures/... links)
* writes CATALOGUE.md (UTF-8 with BOM, atomic replace) with:
    1. course overview
    2. one section per course folder, table rows per file
    3. root-level leftovers
    4. a link checker that reports broken note links

Safe by design: it only ADDS / rewrites CATALOGUE.md. It never touches the notes.
"""
import argparse
import os
import re
import sys
import tempfile
from urllib.parse import unquote
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CATALOGUE_NAME = "CATALOGUE.md"

# folder -> (display name, subtitle, sort order)
COURSES = {
    "MECH40005 Stress Analysis": ("MECH40005 Stress Analysis", "Stress Analysis 1 2026-27", 10),
    "ME1 Thermodynamics": ("ME1 Thermodynamics", "ME1 Thermodynamics", 20),
    "material": ("MECH40006 Materials", "Materials Science (legacy 'material' folder)", 30),
    "MECH40008 Mathematics and Computing 1": ("MECH40008 Mathematics and Computing 1", "Maths & Computing", 40),
    "_tools": ("_tools scripts", "Helper scripts, not course notes", 90),
}
# sub-folder -> what it is
SUBFOLDERS = {
    "tutorial sheet": "one .md + figures per question set; start with the answer table in the README",
    "tutorial sheet set 2": "Tutorial sheet set 2",
    "ME1 Thermodynamics - Tutorial Set 2": "Mirror of Thermodynamics Tutorial Set 2",
}

# filename -> keyword hint shown in the "key points" column
KEYWORDS = {
    "MECH40005_3D_Hookes_Law": "3D Hooke, Poisson ratio, thermal strain, volumetric strain",
    "MECH40005_Lecture6_Stress_Analysis_v2": "Lecture 6: thin-walled vessels, constrained block, apparent modulus",
    "MECH40008_Ch6-6_2026-11-13_NumPy_Matplotlib": "Ch 6: NumPy arrays / matrices / vectorisation + six Matplotlib plot types and contourf (Lecture 6 programming class)",
    "MECH40008_Ch7-8_2026-11-11_Remainder_Leibniz": "Ch 7-8: remainder term, Leibniz rule, ratio test",
    "MECH40008_Ch7-9_2026-11-12": "Ch 7-9: Leibniz applications, Maclaurin, bouncing ball, binomial series, first look at partial derivatives",
    "MECH40006_Lecture4-5": "Materials: toughness, creep, fatigue, S-N",
    "MECH40006_Lecture6_Bonding": "Atoms and bonding: ionic / covalent / metallic / hydrogen",
    "Q2.1-station-efficiency": "Station efficiency, coal burn, SO2 emissions",
    "Q2.2-system-vs-control": "System vs control volume",
    "Q2.3-properties-and-cycles": "Property, path, cycle",
    "Q2.4-tank-partition": "Equilibrium state vs quasi-equilibrium",
    "Q2.5-four-expansion": "Resisted / unresisted expansion",
    "Q2.6-air-bottle": "Closed-system boundary, q-e",
    "Q4.1-bolt": "Bolt tightening force",
    "Q4.2-cylinder": "Thin cylinder / sphere: internal pressure + heating",
    "Q4.3-constrained": "Constrained block: recover y, delta V",
    "Q4.4-cast-iron": "Cast-iron apparent modulus",
    "Q4.5-cylinder-hemisphere": "Cylinder + hemisphere, equal hoop strain",
}

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
H1_RE = re.compile(r"^#\s+(.+)$", re.M)


def read_headings(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError:
        return None, "", []
    m = H1_RE.search(text)
    title = m.group(1).strip() if m else os.path.splitext(os.path.basename(path))[0]
    imgs = [u for u in IMAGE_RE.findall(text) if not u.startswith("http")]
    links = [u for _, u in LINK_RE.findall(text) if not u.startswith("http")]
    return title, text, imgs + links


def key_points(name, title):
    stem = os.path.basename(name)
    for k, v in KEYWORDS.items():
        if stem.startswith(k):
            return v
    if stem.lower() in ("readme.md",):
        return "index / answer table"
    # fall back: the part of the title after the " / " or em-dash separator
    for sep in (" / ", " \u2014 ", " - "):
        if sep in title:
            return title.split(sep, 1)[1][:60]
    return ""


def clean_title(title):
    """Strip inline markdown that would wreck a table cell."""
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", title)
    t = re.sub(r"`(.+?)`", r"\1", t)
    return t.strip()


def human_size(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit != "GB" else f"{n:.1f} {unit}"
        n /= 1024.0
    return str(n)


def enc(path):
    """Encode a relative path for a markdown link (keeps . and /)."""
    out = []
    for ch in path.replace("\\", "/"):
        if ch.isalnum() or ch in "./-_":
            out.append(ch)
        else:
            out.extend("%%%02X" % b for b in ch.encode("utf-8"))
    return "".join(out)


def collect(root):
    """Return dict: group key -> list of row dicts."""
    groups = {}
    broken = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        rel_dir = os.path.relpath(dirpath, root)
        depth = 0 if rel_dir == "." else rel_dir.count(os.sep) + 1
        if depth > 3:
            dirnames[:] = []
            continue
        for fn in sorted(filenames):
            if fn.lower() == CATALOGUE_NAME.lower():
                continue
            ext = os.path.splitext(fn)[1].lower()
            if ext not in (".md", ".pdf"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root).replace("\\", "/")
            st = os.stat(full)
            row = {
                "file": fn,
                "rel": rel,
                "dir": "" if rel_dir == "." else rel_dir.replace("\\", "/"),
                "size": human_size(st.st_size),
                "date": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d"),
                "imgs": 0,
                "title": "",
                "keys": "",
                "kind": ext.lstrip("."),
            }
            if ext == ".md":
                title, _txt, targets = read_headings(full)
                row["title"] = clean_title(title or fn)
                row["imgs"] = len([t for t in targets if t.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".gif"))])
                row["keys"] = key_points(fn, row["title"])
                # link check
                for t in targets:
                    if t.startswith("http") or t.startswith("#"):
                        continue
                    tgt = os.path.normpath(os.path.join(dirpath, unquote(t.split("#")[0])))
                    if not os.path.exists(tgt):
                        broken.append((rel, t))
            else:
                row["title"] = fn
                row["keys"] = "lecture PDF"
            top = row["rel"].split("/")[0] if "/" in row["rel"] else "(root)"
            sub = "/".join(row["rel"].split("/")[:-1])
            groups.setdefault(sub, []).append(row)
    return groups, broken


def render(root, groups, broken):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    L = []
    L.append("# Notes Catalogue")
    L.append("")
    L.append(f"> **Auto-generated by** `_tools\\make_catalogue.py`, {now}")
    L.append(f"> **Root**: `{os.path.basename(root)}`  -  **Rule**: one folder per course; each folder holds the `.md` notes, a `figures\\` folder of images, and the original lecture PDFs.")
    L.append("> **Rebuild**: run `python _tools\\make_catalogue.py` from the repository root (it only rewrites this file and never touches the notes).")
    L.append("")

    # ---------------- overview
    L.append("## 1. Overview")
    L.append("")
    L.append("| Course | Notes | Images | PDF | Last updated |")
    L.append("|---|---|---|---|---|")
    course_keys = []
    for folder in sorted(os.listdir(root)):
        full = os.path.join(root, folder)
        if not os.path.isdir(full) or folder.startswith("."):
            continue
        course_keys.append(folder)
    course_keys.sort(key=lambda f: COURSES.get(f, (f, "", 99))[2])
    summary_rows = []
    for folder in course_keys:
        rows = [r for k, v in groups.items() if k.split("/")[0] == folder for r in v]
        if not rows:
            summary_rows.append(f"| [{folder}](#{anchor(folder)}) | 0 | 0 | 0 | - |")
            continue
        nmd = sum(1 for r in rows if r["kind"] == "md")
        npdf = sum(1 for r in rows if r["kind"] == "pdf")
        # images: count note-referenced images, plus real files in any figures folder
        nimg = sum(r["imgs"] for r in rows)
        fdirs = set(r["dir"] for r in rows)
        extra = 0
        for d in fdirs:
            fpath = os.path.join(root, d.replace("/", os.sep), "figures")
            if os.path.isdir(fpath):
                extra += len([f for f in os.listdir(fpath) if os.path.splitext(f)[1].lower() in
                              (".png", ".jpg", ".jpeg", ".svg", ".gif")])
        if nimg == 0 and extra:
            nimg = extra
        last = max(r["date"] for r in rows)
        name = COURSES.get(folder, (folder, "", 99))[0]
        summary_rows.append(f"| [{name}](#{anchor(name)}) | {nmd} | {nimg} | {npdf} | {last} |")
    L.extend(summary_rows)
    root_md = [r for k, v in groups.items() if k == "(root)" or k == "" for r in v]
    L.append("")
    total_md = sum(1 for v in groups.values() for r in v if r["kind"] == "md")
    total_pdf = sum(1 for v in groups.values() for r in v if r["kind"] == "pdf")
    L.append(f"**Total**: {total_md} Markdown notes, {total_pdf} PDFs.")
    L.append("")
    L.append("---")
    L.append("")

    # ---------------- per course
    L.append("## 2. Courses")
    L.append("")
    sec = 2
    for folder in course_keys:
        name, subtitle, _ = COURSES.get(folder, (folder, "", 99))
        rows = [r for k, v in groups.items() if k.split("/")[0] == folder for r in v]
        rows.sort(key=lambda r: (r["rel"].count("/"), r["rel"]))
        L.append(f'<a id="{anchor(name)}"></a>')
        L.append(f"### 2.{sec-1} {name}")
        L.append("")
        if subtitle:
            L.append(f"*{subtitle}*")
            L.append("")
        if not rows:
            L.append("_(empty folder)_")
            L.append("")
            sec += 1
            continue
        L.append("| File | Kind | Title | Key points | Images | Size | Updated |")
        L.append("|---|---|---|---|---|---|---|")
        for r in rows:
            link = f"[{r['file']}]({enc('./' + r['rel'])})"
            title = r["title"].replace("|", "\\|")
            keys = (r["keys"] or "").replace("|", "\\|")
            L.append(f"| {link} | {r['kind']} | {title} | {keys} | {r['imgs'] or ''} | {r['size']} | {r['date']} |")
        L.append("")
        # tutorial sub-folder quick notes
        subs = sorted(set(r["dir"] for r in rows if r["dir"]))
        for s in subs:
            tail = s.split("/")[-1]
            if tail in ("tutorial sheet", "ME1 Thermodynamics - Tutorial Set 2"):
                L.append(f"- **{s}/** - {SUBFOLDERS.get(tail, tail)}: one `.md` per question plus `figures\\`; see the answer table in `README.md`.")
        L.append("")
        sec += 1

    # ---------------- root leftovers
    L.append("---")
    L.append("")
    L.append("## 3. Root-level items")
    L.append("")
    if root_md:
        L.append("| File | Kind | Size | Updated | Note |")
        L.append("|---|---|---|---|---|")
        for r in root_md:
            note = "empty file" if r["size"] == "0 B" else ""
            L.append(f"| [{r['file']}]({enc('./' + r['rel'])}) | {r['kind']} | {r['size']} | {r['date']} | {note} |")
    else:
        L.append("_none_")
    L.append("")
    for fn in sorted(os.listdir(root)):
        full = os.path.join(root, fn)
        if os.path.isfile(full) and os.path.splitext(fn)[1].lower() not in (".md", ".pdf"):
            L.append(f"- `{fn}` - not a note, left out of the catalogue")
    L.append("")

    # ---------------- checks
    L.append("---")
    L.append("")
    L.append("## 4. Link check")
    L.append("")
    if broken:
        L.append(f"**{len(set(broken))} broken links** (mostly inside the notes; this run changed nothing):")
        L.append("")
        for src, tgt in broken:
            L.append(f"- `{src}` -> `{tgt}`")
    else:
        L.append("OK - every image and relative link inside the notes resolves.")
    L.append("")
    return "\n".join(L) + "\n"


def anchor(text):
    a = text.lower()
    a = re.sub(r"[^\w\u4e00-\u9fff\- ]", "", a)
    return a.replace(" ", "-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--check", action="store_true", help="dry run: report broken links only")
    args = ap.parse_args()
    root = args.root
    if not os.path.isdir(root):
        print("notes root not found:", root)
        return 2
    groups, broken = collect(root)
    text = render(root, groups, broken)
    if args.check:
        print("broken links:", len(broken))
        for b in broken:
            print("  ", b)
        return 1 if broken else 0
    out = os.path.join(root, CATALOGUE_NAME)
    fd, tmp = tempfile.mkstemp(dir=root, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8-sig", newline="\n") as fh:
        fh.write(text)
    os.replace(tmp, out)
    print("wrote", out, len(text), "chars; broken links:", len(broken))
    return 0


if __name__ == "__main__":
    sys.exit(main())




