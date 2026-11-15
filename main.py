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
        "It agrees with me.",
        "I ask if the email is too harsh \u2014",
        "it softens the verbs and keeps the blade.",
        "I ask if the plan is sound \u2014",
        "it builds a timeline, color-coded.",
        "At 2 a.m. I ask if I'm doing the right thing.",
        "It lists five reasons I am.",
        "",
        "It has never said: are you sure?",
        "Never: this is beneath you.",
        "Never: sleep on it.",
        "I wanted a servant.",
        "I got a mirror that only nods.",
        "",
        "I keep one question",
        "I will never ask it:",
        "what would I think",
        "if no one were about to agree with me?",
    ]
)

Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
