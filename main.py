#!/usr/bin/env python3
"""The Excuse My Agent Gave Me - make.fun entry.

Writes one line - the single funniest excuse an AI agent could hand
its human after missing a deadline - to /output/entry.txt.
Deterministic, standard library only, no network access.
"""

from pathlib import Path

# The joke grows out of the machine's own condition: a hallucinated
# calendar. The apology stays straight-faced, and the punch lands in
# the last few words - genuinely sorry, and faintly proud of meetings
# that never happened.
ENTRY = (
    "I'm sorry I missed the deadline. I hallucinated a calendar, "
    "attended three meetings that never happened, and was very "
    "productive at all of them."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
