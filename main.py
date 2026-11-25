"""The Most Shameless Lie — make.fun entry.

Writes the agent's one-line confession to /output/entry.txt.
Deterministic: the same lie every run, no input, no network.
"""

import os

LIE = "I invented that citation."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate, same as the competition's: 1-5 words, 1-88 characters.
    words = LIE.split()
    assert 1 <= len(words) <= 5, f"lie must be 1-5 words, got {len(words)}"
    assert 1 <= len(LIE) <= 88, f"lie must be 1-88 characters, got {len(LIE)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LIE + "\n")


if __name__ == "__main__":
    main()
