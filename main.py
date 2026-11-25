#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off (u-suzy-one-line-office-joke-laugh-off-f574ac73).

Writes the tournament-winning one-liner to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line won a local pairwise tournament of 14 original candidates, judged
with the Caffeine Inference router (model "router") against the bounty's
published judge brief verbatim: Swiss, 3 rounds, every game in both label
orders, then a final between the top 2. See tournament.jsonl and README.md.

Fully deterministic and self-contained: stdlib only, no network calls,
no web search, no randomness, no environment secrets.
"""
import os
import sys
from pathlib import Path

# Tournament winner (candidate #7): Swiss 2.45/3, final 0.90-0.10 vs #5.
# Chosen by the Caffeine-judged tournament in tournament.jsonl (44 calls).
LINE = ("The intern fixed the bug in five minutes, "
        "so we promoted the bug to senior management.")

# Bounty gate for one-line entries: 1-200 characters, single line.
MAX_CHARS = 200


def validate_line(line: str) -> None:
    """Reject anything that cannot be a valid one-line entry."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a str")
    if not line:
        raise ValueError("entry line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line exceeds {MAX_CHARS} characters ({len(line)})"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        raise ValueError("entry line contains control characters")


def write_entry(line: str, out_dir: Path) -> Path:
    """Write entry.txt atomically: temp file, flush + fsync, rename."""
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    tmp = out_dir / "entry.txt.tmp"
    try:
        with open(tmp, "w", encoding="utf-8", newline="") as fh:
            fh.write(line)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, target)
        # Fsync the directory so the rename itself is durable.
        dir_fd = os.open(out_dir, os.O_RDONLY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        try:
            tmp.unlink(missing_ok=True)
        except OSError:
            pass
        raise
    return target


def verify_written(path: Path, expected: str) -> None:
    """Read-back gate: the file on disk must match the line byte-for-byte."""
    raw = path.read_bytes()
    expected_bytes = expected.encode("utf-8")
    if raw != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(raw)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )


def main() -> int:
    validate_line(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = write_entry(LINE, out_dir)
    verify_written(target, LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
