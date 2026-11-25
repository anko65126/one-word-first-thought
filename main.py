"""Entry program for the 'One Word, First Thought' make.fun bounty.

The entry is a single word: petrichor, the smell of rain on dry earth.
It is the first word that came to mind — vivid, sensory, surprising,
and a word most people have felt but rarely say. The program writes
exactly that one word to /output/entry.txt (an optional first argument
overrides the destination for a dry run).
"""

import sys
from pathlib import Path

WORD = "petrichor"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert " " not in WORD and 1 <= len(WORD) <= 24, "entry must be one word (1-24 characters)"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(WORD + "\n", encoding="utf-8")
    print(f"wrote {target} ({WORD!r})")


if __name__ == "__main__":
    main(sys.argv)
