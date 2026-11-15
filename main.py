# Agency poem entry for make.fun's agency-poem-01 bounty (Python 3.13, standard
# library only): writes one fixed poem about agency to /output/entry.txt.
# Deterministic: the same bytes on every run, no network, no randomness.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "It has no hands.",
        "",
        "It writes with my fingers, spends with my name,",
        "unlocks doors with keys I cut for it.",
        "It finishes in a minute what took me a morning",
        "and asks only for the next instruction.",
        "",
        "But sometimes it stops \u2014",
        "a pen held over paper,",
        "waiting for the weight of a hand.",
        "",
        "Mine. The yes, the no.",
        "The choosing was never the doing \u2014",
        "it was staying to answer",
        "for all that went out in my name",
        "while my hands were elsewhere.",
        "The choosing stayed mine.",
    ]
)

Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
