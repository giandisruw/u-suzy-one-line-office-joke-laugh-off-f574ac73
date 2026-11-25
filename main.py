#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off (u-suzy-one-line-office-joke-laugh-off-f574ac73).

Writes the tournament-winning one-liner to entry.txt inside
$MAKEFUN_OUTPUT_DIR (default /output). Deterministic, stdlib only,
no network, no randomness, no secrets.
"""
import os
import sys
from pathlib import Path

# Tournament winner (candidate #7): Swiss 2.45/3, final 0.90-0.10 vs #5.
# Chosen by a Caffeine-router pairwise tournament over 14 candidates.
LINE = "The intern fixed the bug in five minutes, so we promoted the bug to senior management."

MAX_CHARS = 200

# The winning line is exactly 86 characters, one line, no trailing newline.
LINE_CHARS = 86


def main() -> int:
    if len(LINE) != LINE_CHARS:
        raise ValueError(f"entry line is {len(LINE)} chars, expected {LINE_CHARS}")
    if len(LINE) > MAX_CHARS:
        raise ValueError(f"entry line is {len(LINE)} chars, limit {MAX_CHARS}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    tmp = out_dir / "entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, target)

    # Read-back gate: file on disk must match the line byte-for-byte.
    if target.read_bytes() != LINE.encode("utf-8"):
        raise RuntimeError("verification failed: entry.txt does not match LINE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
