"""Quarto post-render step: drop prev/next page links that point at draft pages.

Quarto leaves drafts (`draft: true`) out of listings, the sidebar and search, but the
prev/next page navigation still links to their empty output. This removes those links.
Runs from `project.post-render` in _quarto.yml.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site")
DRAFT_STUB = re.compile(r"^\s*<!DOCTYPE html>\s*<html[^>]*>\s*</html>\s*$", re.IGNORECASE)
NAV_LINK = re.compile(r'(<div class="nav-page nav-page-(?:previous|next)">)\s*<a href="([^"]+)".*?</a>', re.DOTALL)
HEAD_LINK = re.compile(r'<link href="([^"]+)" rel="(?:next|prev)">\n?')


def is_draft(path: Path) -> bool:
    return path.stat().st_size < 512 and bool(DRAFT_STUB.match(path.read_text(encoding="utf-8")))


def main() -> None:
    pages = list(SITE.rglob("*.html"))
    drafts = {p.resolve() for p in pages if is_draft(p)}
    if not drafts:
        return
    fixed = 0
    for page in pages:
        if page.resolve() in drafts:
            continue
        text = page.read_text(encoding="utf-8")

        def points_at_draft(href: str) -> bool:
            return (page.parent / href.split("#")[0]).resolve() in drafts

        new = NAV_LINK.sub(lambda m: m.group(1) if points_at_draft(m.group(2)) else m.group(0), text)
        new = HEAD_LINK.sub(lambda m: "" if points_at_draft(m.group(1)) else m.group(0), new)
        if new != text:
            page.write_text(new, encoding="utf-8")
            fixed += 1
    print(f"strip_draft_links: {len(drafts)} drafts, fixed links on {fixed} pages")


if __name__ == "__main__":
    main()
