# -*- coding: utf-8 -*-
"""Math-style gate for the notes: formulas must be Markdown math, never plain text."""
import re, io, sys, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOTS = [d for d in sorted(glob.glob(os.path.join(ROOT, "*"))) if os.path.isdir(d)]
SKIP = ("_work", "_tools")
FORMULA_HINT = re.compile(r"\^|_\{|_\w|\\frac|sum|lim_|sqrt|C\(|exp\(|\bR_n\b|<=|>=|\u2192|\u2265|\u2264|\u221e|\u03a3|\u221a|\u00d710")
TEXT_FENCE = "```text"

def check(path):
    s = io.open(path, encoding="utf-8").read()
    name = os.path.basename(path)
    problems = []
    if s.count(TEXT_FENCE):
        problems.append("%d text fence(s) used for formulas" % s.count(TEXT_FENCE))
    spans = re.findall(r"`([^`\n]+)`", s)
    bad = [x for x in spans if FORMULA_HINT.search(x)]
    if bad:
        problems.append("%d backtick formula span(s): %s" % (len(bad), "; ".join(bad[:4])))
    chinese_text = re.findall(r"\\text\{[^}]*[\u3400-\u9fff][^}]*\}", s)
    if chinese_text:
        problems.append("Chinese inside a math text command: " + "; ".join(chinese_text[:3]))
    if s.count("$") % 2:
        problems.append("odd number of dollar signs (%d) - unbalanced inline math" % s.count("$"))
    if re.search(r"\\newcommand|\\label\{|\\begin\{align(?!ed)", s):
        problems.append("newcommand/label/align is not supported by the renderer")
    return name, s.count("$$") // 2, (s.count("$") - 2 * s.count("$$")) // 2, problems

files = sorted(f for r in ROOTS for f in glob.glob(os.path.join(r, "*.md")))
fails = 0
print("%-64s %7s %7s %7s" % ("file", "blocks", "inline", "status"))
for f in files:
    if any(t in f for t in SKIP):
        continue
    name, blocks, inline, probs = check(f)
    if probs:
        fails += 1
        print("%-64s %7d %7d %7s" % (name[:64], blocks, inline, "FAIL"))
        for p in probs:
            print("    - " + p)
    else:
        print("%-64s %7d %7d %7s" % (name[:64], blocks, inline, "OK"))
print()
print("RESULT PASS" if fails == 0 else "RESULT FAIL(%d)" % fails)
sys.exit(1 if fails else 0)
