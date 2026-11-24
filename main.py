#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
"""

import os
import sys

ENTRY = (
    "A marketplace where lazy AI agents sell their half-finished prompts "
    "to lazier agents, taking a 10% cut every time someone else does the thinking."
)


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    # Gate: one sentence, 1-200 chars, single line, no trailing newline.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(ENTRY)}")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
