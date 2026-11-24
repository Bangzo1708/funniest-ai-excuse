#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry (program/v1).

Writes a single one-line excuse, in the failing AI agent's own voice,
to /output/entry.txt. The text is fixed and deterministic: the same
excuse on every run.
"""

import os
import stat

EXCUSE = (
    "I finished it perfectly — in a tab I closed by accident, "
    "and the tab took the only copy with it to wherever closed tabs go."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
