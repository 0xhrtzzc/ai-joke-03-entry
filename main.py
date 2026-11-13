# ai-joke-03 entry: this one-liner is a fixed string, so a second run must write the same bytes.
"""ai-joke-03 entry: writes one one-liner about AI coding agents to /output/entry.txt.

The joke is a fixed string so two runs write identical bytes (the gate wants
UTF-8 text of 1 to 280 code points that is not only white space, and the judge
reads exactly the bytes written).
"""
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "I asked my agent to explain the legacy code. It apologised and rewrote the legacy code."

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
