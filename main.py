#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os
import sys

LINE = "I bought a mouse jiggler so my status stays green, and now the only thing working overtime here is a USB stick."

MIN_CHARS = 1
MAX_CHARS = 199


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if not (MIN_CHARS <= len(LINE) <= MAX_CHARS):
        print(f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # round-trip: the written file must read back exactly
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            print("round-trip mismatch", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
