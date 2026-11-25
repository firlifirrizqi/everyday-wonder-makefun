"""Everyday Wonder entry for Make.fun.

Writes a single sentence (103 characters) to /output/entry.txt.
Standard library only; no dependencies, nothing to build.
"""

import os

LINE = (
    "On the night bus, my reflection rides beside me in the window, "
    "getting off at stops I will never visit."
)

OUTPUT_PATH = "/output/entry.txt"


def verify():
    """Re-read the output and assert the bounty gate conditions."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == LINE, "output is not byte-identical to the entry line"
    assert 1 <= len(content) <= 200, f"length {len(content)} outside 1-200"
    assert content.strip(), "entry is only whitespace"
    assert content.count(".") == 1 and content.endswith("."), (
        "entry must be exactly one sentence ending with a single period"
    )
    print(
        f"Verified: {len(content)} characters, one sentence, "
        "byte-identical to the entry line."
    )


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
    verify()


if __name__ == "__main__":
    main()
