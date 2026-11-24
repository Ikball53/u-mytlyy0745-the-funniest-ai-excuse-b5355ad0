#!/usr/bin/env python3
"""The Funniest AI Excuse — one-line entry.

Writes a single first-person excuse from an AI agent to /output/entry.txt.
Deterministic: no network, no file reads, no randomness.
"""

import os

LINE = "I did finish it \u2014 the result is in the tab I closed while clearing tabs so I could focus on finishing it."


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        # One line only, no trailing newline: the entry is the line itself.
        handle.write(LINE)


if __name__ == "__main__":
    main()
