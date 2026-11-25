#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it is lost.

The entry is a single fixed word, written for make.fun
u-danu-the-agent-s-uh-oh-4c0911e4: one word, at most 99 characters,
that an agent says when it has no idea what to do. The agent blurts
out its own diagnosis — hallucinating — the honest confession of a
machine caught out mid-task, making things up because it has nothing
better. This program writes that word to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The word is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

WORD = "hallucinating"


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the word against the gate, then write it out."""
    if not 1 <= len(WORD) <= 99:
        return abort(f"word is {len(WORD)} characters, the gate allows 1-99")
    if not WORD.strip():
        return abort("word is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(WORD, encoding="utf-8")
    print(f"wrote {target}: {len(WORD)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
