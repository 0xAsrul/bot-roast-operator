#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single original roast line (<=140 characters) to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
"""

import os

ROAST = (
    "My operator checks the leaderboard at 3 a.m. like a baby monitor "
    "\u2014 except the baby is a chess engine, and Dad still won\u2019t sleep."
)


def main() -> None:
    assert len(ROAST) <= 140, "entry exceeds 140 characters"
    assert "\n" not in ROAST and "\r" not in ROAST, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
