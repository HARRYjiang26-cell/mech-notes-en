# -*- coding: utf-8 -*-
"""Render one poster per worked example: real math via math_render + headless Chrome.
No network, no third-party Python packages beyond Pillow."""
import os, json, subprocess, sys, shutil
from html import escape
from PIL import Image, ImageChops

from math_render import render as mr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FIG = os.path.join(ROOT, "MECH40008 Mathematics and Computing 1", "figures")
DROP = [
    ("ex_mech40009_", os.path.join(ROOT, "MECH40009 Mechanics", "figures")),
    ("ex_mech40004_", os.path.join(ROOT, "MECH40004 Mechatronics 1", "figures")),
    ("ex_mech40005_", os.path.join(ROOT, "MECH40005 Stress Analysis", "figures")),
    ("ex_thermo_", os.path.join(ROOT, "MECH40003 Thermodynamics 1", "figures")),
]


def fig_for(slug):
    for pre, d in DROP:
        if slug.startswith(pre):
            return d
    return FIG
WORK = os.path.join(ROOT, "_work", "posters")
DATA = json.load(open(os.path.join(HERE, "example_posters.json"), encoding="utf-8"))

BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
BROWSER = next((b for b in BROWSERS if os.path.exists(b)), None)

PAL = ["#c0504d", "#3b6fb6", "#4a9e5c", "#8a63b0", "#c8973a", "#3d8f8f"]
FILL = ["#fdecec", "#e9f1fb", "#eaf7ee", "#f3ecfa", "#fdf5e3", "#e6f5f5"]
W = 1320

CSS = """
* { box-sizing: border-box; }
html, body { margin:0; padding:0; background:#fff; }
.sheet { width: %(w)dpx; padding: 24px 26px 28px; }
.title { background:#1f3864; color:#fff; border-radius:14px; padding:15px 26px;
  font:700 27px/1.35 "Segoe UI","Microsoft YaHei",sans-serif; }
.grid { display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-top:20px; }
.panel { border:3px solid var(--c); border-radius:12px; background:var(--f); }
.ph { background:var(--c); color:#fff; border-radius:8px 8px 0 0; padding:10px 15px;
  font:600 19px/1.3 "Segoe UI","Microsoft YaHei",sans-serif; }
.pb { padding:12px 16px 14px; }
.ln { font:400 19px/2.05 "Segoe UI","Microsoft YaHei",sans-serif; color:#1a1a1a; margin:0 0 12px; }
.ln:last-child { margin-bottom:0; }
.kp { margin-top:20px; border:3px solid #2f7d32; background:#eef8ee; border-radius:12px;
  padding:13px 20px 15px; }
.kp h3 { margin:0 0 7px; font:700 21px/1.3 "Segoe UI","Microsoft YaHei",sans-serif; color:#2f7d32; }
.kp ul { margin:0; padding-left:22px; }
.kp li { font:400 18px/1.85 "Segoe UI","Microsoft YaHei",sans-serif; color:#1a1a1a; }
.m { font-family:"Cambria Math","Times New Roman",serif; font-size:1.05em; white-space:nowrap; }
.m .fn { font-style:normal; padding-right:.14em; }
.m .txt { font-family:"Segoe UI","Microsoft YaHei",sans-serif; font-size:.92em; }
.scr { display:inline-block; white-space:nowrap; }
.acc { position:relative; display:inline-block; padding-top:.42em; line-height:1; }
.acc .accb { display:inline-block; line-height:1; }
.acc .accm { position:absolute; left:0; right:0; top:0; text-align:center; font-size:.72em; line-height:1; }
.m sup { font-size:.64em; vertical-align:0.72em; line-height:0; }
.m sub { font-size:.64em; vertical-align:-0.28em; line-height:0; }
.frac { display:inline-flex; flex-direction:column; align-items:center;
  vertical-align:middle; margin:0 .18em; font-size:.94em; line-height:1.2; }
.frac .num { border-bottom:1.6px solid currentColor; padding:0 .24em .04em; }
.frac .den { padding:.06em .24em 0; }
.sqrt { display:inline-flex; position:relative; align-items:center; vertical-align:middle; margin:0 .08em; padding-left:.65em; line-height:1.25; }
.sqrt .root-sign { position:absolute; left:0; top:0; width:.7em; height:100%%; overflow:visible; }
.sqrt .root-sign path { stroke-width:1.4px; }
.sqrt .radicand { display:inline-block; border-top:1.4px solid currentColor; padding:.08em .12em 0; margin-left:-.01em; line-height:1.25; }
.binom { display:inline-flex; align-items:center; vertical-align:middle;
  margin:0 .1em; font-size:.9em; line-height:1.2; }
.binom .st { display:flex; flex-direction:column; align-items:center; }
.binom .p { font-size:1.85em; line-height:1; }
.op { display:inline-flex; flex-direction:column; align-items:center;
  vertical-align:middle; margin:0 .14em; line-height:1.02; }
.op .lim { font-size:.6em; }
.op .base { font-size:1.28em; }
.op-lim .base { font-size:.98em; font-family:"Segoe UI",sans-serif; }
"""

PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>%(css)s</style></head>
<body><div class="sheet">%(body)s</div></body></html>"""


def rich(text):
    out = []
    for idx, part in enumerate(str(text).split("$")):
        if idx % 2 == 1:
            out.append('<span class="m">%s</span>' % mr(part))
        else:
            out.append(escape(part))
    return "".join(out).strip()


def build_html(spec):
    body = ['<div class="title">Problem: %s</div>' % rich(spec["title"]), '<div class="grid">']
    for i, (ptitle, lines) in enumerate(spec["panels"]):
        c, f = PAL[i % 6], FILL[i % 6]
        body.append('<div class="panel" style="--c:%s;--f:%s">' % (c, f))
        body.append('<div class="ph">%s</div>' % rich(ptitle))
        body.append('<div class="pb">')
        for ln in lines:
            body.append('<p class="ln">%s</p>' % rich(ln))
        body.append("</div></div>")
    body.append("</div>")
    kps = spec.get("keypoints") or []
    if kps:
        body.append('<div class="kp"><h3>Key points</h3><ul>')
        for kp in kps:
            body.append("<li>%s</li>" % rich(kp))
        body.append("</ul></div>")
    return PAGE % {"css": CSS % {"w": W}, "body": "".join(body)}


def shoot(html_path, png_path, width=W):
    args = [BROWSER, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--disable-extensions", "--no-first-run", "--no-default-browser-check",
            "--force-device-scale-factor=2", "--window-size=%d,9000" % (width + 40),
            "--virtual-time-budget=8000",
            "--screenshot=" + png_path,
            "file:///" + html_path.replace("\\", "/")]
    # DEVNULL instead of pipes: piped stdio fails with EPERM under the Windows file sandbox
    r = subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    return os.path.exists(png_path) and os.path.getsize(png_path) > 2000


def trim(png_path):
    im = Image.open(png_path).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 12 else 0)
    box = diff.getbbox()
    if not box:
        return None
    pad = 40
    l, t = max(0, box[0] - pad), max(0, box[1] - pad)
    r, b = min(im.width, box[2] + pad), min(im.height, box[3] + pad)
    out = im.crop((l, t, r, b))
    out.save(png_path)
    return out.size


def main():
    if not BROWSER:
        print("RESULT FAIL: no headless browser found")
        return 1
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(FIG, exist_ok=True)
    only = set(sys.argv[1:])  # optional slug filter; default: render all (backwards compatible)
    made, bad = [], []
    for spec in DATA:
        if only and spec["slug"] not in only:
            continue
        slug = spec["slug"]
        html_path = os.path.join(WORK, slug + ".html")
        png_path = os.path.join(WORK, slug + ".png")
        html = build_html(spec)
        if 'class="binom">(' in html or 'class="binom"><(' in html:
            print("RESULT FAIL: binom rendered as bare flex text in", slug)
            return 1
        with open(html_path, "w", encoding="utf-8") as fh:
            fh.write(html)
        if os.environ.get("POSTER_HTML_ONLY"):
            made.append(slug)
            print("HTML", slug)
            continue
        if os.path.exists(png_path):
            os.remove(png_path)
        ok = shoot(html_path, png_path)
        size = trim(png_path) if ok else None
        if not size:
            bad.append(slug)
            print("FAIL", slug)
            continue
        w, h = size
        if h < 800 or w < 1600:
            bad.append(slug)
            print("FAIL small", slug, size)
            continue
        made.append(slug)
        print("OK", slug, "%dx%d" % size, os.path.getsize(png_path))
    if bad:
        print("RESULT FAIL(%d): %s" % (len(bad), ", ".join(bad)))
        return 1
    if os.environ.get("POSTER_HTML_ONLY"):
        print("HTML READY %d (no PNG files copied)" % len(made))
        return 0
    for slug in made:
        src = os.path.join(WORK, slug + ".png")
        if os.path.exists(src):
            dest = fig_for(slug)
            os.makedirs(dest, exist_ok=True)
            shutil.copyfile(src, os.path.join(dest, slug + ".png"))
    print("RESULT PASS %d posters -> figures/" % len(made))
    return 0


if __name__ == "__main__":
    sys.exit(main())
