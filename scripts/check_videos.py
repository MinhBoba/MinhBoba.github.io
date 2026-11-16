"""Check that every YouTube video embedded with {{< video >}} can play on this site.

YouTube's oEmbed endpoint answers 200 for embeddable videos, 401 when the owner
has disabled embedding, and 404 when the video is private or deleted.

Usage:  python scripts/check_videos.py        (exit code 1 if any video fails)
"""

from __future__ import annotations

import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_RE = re.compile(r"\{\{<\s*video\s+(\S+)")
YOUTUBE_RE = re.compile(r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([\w-]{11})")
SKIP_DIRS = {"_site", "_freeze", ".quarto", ".git", ".claude", "node_modules"}

REASONS = {401: "embedding disabled by owner", 403: "embedding disabled by owner", 404: "private or deleted"}


def embed_status(video_id: str) -> int:
    url = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(
        f"https://www.youtube.com/watch?v={video_id}", safe=""
    )
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            return resp.status
    except urllib.error.HTTPError as err:
        return err.code


def main() -> int:
    failures = 0
    checked = 0
    for qmd in sorted(ROOT.rglob("*.qmd")):
        if SKIP_DIRS.intersection(qmd.relative_to(ROOT).parts):
            continue
        for line_no, line in enumerate(qmd.read_text(encoding="utf-8").splitlines(), start=1):
            for target in VIDEO_RE.findall(line):
                match = YOUTUBE_RE.search(target)
                if not match:
                    continue
                checked += 1
                status = embed_status(match.group(1))
                if status != 200:
                    failures += 1
                    reason = REASONS.get(status, f"HTTP {status}")
                    print(f"FAIL {qmd.relative_to(ROOT)}:{line_no}  {match.group(1)}  ({reason})")
    print(f"Checked {checked} YouTube embed(s); {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
