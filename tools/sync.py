#!/usr/bin/env python3
"""Copy the shared header and footer into every page.

Edit tools/partials/header.html or tools/partials/footer.html, then run this
from the project folder:

    python3 tools/sync.py

To update only some pages, list them:

    python3 tools/sync.py about/index.html blog/index.html

Pages are only touched between their <!-- header:start/end --> and
<!-- footer:start/end --> markers. The current page's menu link is marked
with aria-current so it shows as selected.
"""
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
partials = root / "tools" / "partials"
header = (partials / "header.html").read_text(encoding="utf-8").strip()
footer = (partials / "footer.html").read_text(encoding="utf-8").strip()
skip_dirs = {"tools", "reference", ".git", ".claude"}

only = {(pathlib.Path.cwd() / a).resolve() for a in sys.argv[1:]}
changed = 0
for page in sorted(root.rglob("*.html")):
    if only and page.resolve() not in only:
        continue
    rel = page.relative_to(root)
    if rel.parts[0] in skip_dirs:
        continue
    html = page.read_text(encoding="utf-8")
    if "<!-- header:start -->" not in html:
        continue  # redirect pages and other standalone files
    if rel.name == "index.html":
        url = "/" if str(rel.parent) == "." else f"/{rel.parent.as_posix()}/"
    else:
        url = f"/{rel.as_posix()}"
    page_header = header
    if url != "/":
        page_header = header.replace(f'<a href="{url}">', f'<a href="{url}" aria-current="page">')
    new = re.sub(r"<!-- header:start -->.*?<!-- header:end -->", lambda m: page_header, html, flags=re.S)
    new = re.sub(r"<!-- footer:start -->.*?<!-- footer:end -->", lambda m: footer, new, flags=re.S)
    if new != html:
        page.write_text(new, encoding="utf-8")
        changed += 1
        print(f"updated {rel}")
print(f"{changed} page(s) updated")
