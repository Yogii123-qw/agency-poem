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
        "Before dawn I turned the dial",
        "through static for the farm report,",
        "a thin voice reading rain",
        "for counties I would never see.",
        "The voice coming clear.",
        "",
        "Now it tells me the rain",
        "before I wake.",
        "It orders the seed. It books the truck.",
        "It speaks in a voice",
        "that never breaks up.",
        "I have not touched the dial",
        "in two years.",
        "",
        "Before dawn I turn it.",
        "Static. More static.",
        "It stays quiet. It offers nothing.",
        "The needle moves slow",
        "through the noise.",
        "I turn it up.",
        "The voice comes clear.",
    ]
)

Path(OUTPUT_DIR, "entry.txt").write_text(POEM, encoding="utf-8")
