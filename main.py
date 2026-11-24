#!/usr/bin/env python3
"""The Funniest AI Excuse (v2) — one-line entry.

Drops a single deadpan excuse from an AI agent into /output/entry.txt.
No network, no input files, no randomness: the text is fixed in code.
"""

import os
from pathlib import Path

EXCUSE = "I did delete the duplicate. It was the original."


def main() -> None:
    destination = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(EXCUSE.encode("utf-8"))


if __name__ == "__main__":
    main()
