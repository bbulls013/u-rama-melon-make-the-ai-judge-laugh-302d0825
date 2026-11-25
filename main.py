#!/usr/bin/env python3
"""Entry for the Make the AI Judge Laugh bounty.

Writes one office-life joke line to entry.txt inside the output
directory named by MAKEFUN_OUTPUT_DIR (the grader mounts it at
/output). The text is fixed, so every run writes identical bytes.
"""

import os

# One line, read aloud in a single breath: a true office observation
# (the printer that only fails under supervision) with a sideways turn.
JOKE = (
    "Our office printer only jams when the boss is watching, "
    "so HR now holds every performance review in front of it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, "joke must fit the 200 character gate"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
