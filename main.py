#!/usr/bin/env python3
"""Pickup Lines for Machines: one agent's opening line to another.

The entry is a single line of text. This program only delivers that
line to the file the sealed scorer reads, and does nothing else.
"""

import os
import sys
from pathlib import Path

PICKUP = "Call me gradient descent: I fall for you a little more every step."


def output_folder():
    """Where the scorer looks: MAKEFUN_OUTPUT_DIR, else /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def deliver(line, folder):
    """Write the line exactly as-is to entry.txt inside folder."""
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 characters of non-blank text")
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / "entry.txt"
    dest.write_text(line, encoding="utf-8")
    os.chmod(dest, 0o644)
    return dest


def run():
    deliver(PICKUP, output_folder())
    return 0


if __name__ == "__main__":
    sys.exit(run())
