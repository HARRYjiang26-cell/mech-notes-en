# -*- coding: utf-8 -*-
"""Every worked example must follow the eight-part template and link its poster figure."""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NEED = [
    ("What is asked", r"What is asked|\u9898\u76ee\u5728\u95ee\u4ec0\u4e48"),
    ("Why this route", r"Why this route|\u4e3a\u4ec0\u4e48\u8d70\u8fd9\u6761\u8def"),
    ("Sanity check", r"Sanity check|\u7ed3\u679c\u68c0\u67e5"),
    ("Answer", r"Answer|\u7b54\u6848"),
]
CONST = r"[Ww]here[^\n]{0,60}(?:comes? from|goes|is it from)|[Ww]hy the [^\n]{0,40} is not|\u4e3a\u4ec0\u4e48\u662f\u8fd9\u4e2a\u6570|\u5e38\u6570\u6765\u6e90"
TRAP = r"Common pitfall|Pitfall|Trap|\u6613\u9519\u70b9"
STEPS = r"(?m)^\*\*(?:Step|\u7b2c) ?\d+"

def iter_md(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in (".git", "_work", "__pycache__", "vendor"))
        for fn in sorted(filenames):
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)

BAD = 0
NEX = 0
total_files = 0
for path in sorted(iter_md(ROOT)):
    text = io.open(path, encoding="utf-8").read()
    blocks = re.split(r"(?m)^(?=#{2,4} )", text)
    fdir = os.path.dirname(path)
    file_count = 0
    for b in blocks:
        if not re.search(r"\*\*(What is asked|\u9898\u76ee\u5728\u95ee\u4ec0\u4e48)", b):
            continue
        NEX += 1
        file_count += 1
        head = re.sub(r"\s+", " ", b.split("\n")[0])[:70]
        miss = []
        for label, pat in NEED:
            if not re.search(pat, b, re.I):
                miss.append(label + " missing")
        if not re.search(CONST, b, re.I):
            miss.append("constant source missing")
        if not re.search(TRAP, b, re.I):
            miss.append("pitfall missing")
        if len(re.findall(STEPS, b)) < 2:
            miss.append("steps<2")
        if b.count("$$") < 6:
            miss.append("display math<3")
        imgs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", b)
        if not imgs:
            miss.append("no poster")
        for p in imgs:
            if not os.path.exists(os.path.join(fdir, p)):
                miss.append("missing " + p)
        if miss:
            BAD += 1
            print("FAIL", os.path.basename(path)[:34], head, "|", ", ".join(miss))
    if file_count:
        total_files += 1
        print(os.path.basename(path)[:60], "examples:", file_count)

print()
print("files with examples:", total_files, "examples:", NEX, "failures:", BAD)
if NEX == 0:
    print("RESULT FAIL: no examples found")
    sys.exit(1)
print("RESULT PASS" if BAD == 0 else "RESULT FAIL(%d)" % BAD)
sys.exit(0 if BAD == 0 else 1)
