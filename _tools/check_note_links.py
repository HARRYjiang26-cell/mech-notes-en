"""Check note links: every local image reference and local file link must exist."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMG_HTML = re.compile(r'<img\s+src="([^"]+)"')
IMG_MD = re.compile(r'!\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
LINK_MD = re.compile(r'\]\(((?:\.\.?/)[^)#]+|figures/[^)#]+)\)')

def iter_md(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "_work", "__pycache__", "vendor")]
        for fn in sorted(filenames):
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)

bad = 0
checked = 0
for path in sorted(iter_md(ROOT)):
    base = os.path.dirname(path)
    text = open(path, encoding="utf-8").read()
    refs = IMG_HTML.findall(text) + IMG_MD.findall(text) + LINK_MD.findall(text)
    refs = [r for r in refs if not r.startswith(("http://", "https://", "mailto:"))]
    if not refs:
        continue
    checked += 1
    missing = []
    for r in refs:
        target = os.path.normpath(os.path.join(base, r.replace("%20", " ")))
        if not os.path.exists(target):
            missing.append(r)
    rel = os.path.relpath(path, ROOT)
    if missing:
        bad += len(missing)
        print("DEAD", rel)
        for m in missing:
            print("    ->", m)
    else:
        print("OK  ", rel, "refs:", len(refs))

print()
print("files with links:", checked)
print("RESULT", "PASS" if bad == 0 else "FAIL(%d)" % bad)
sys.exit(0 if bad == 0 else 1)
