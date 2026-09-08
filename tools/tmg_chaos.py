#!/usr/bin/env python3
"""TMG Chaos Engine: objectively unnecessary, surprisingly entertaining."""

from __future__ import annotations

import random


TMG_EVENTS = [
    "TMG opened one more project instead of finishing the current one.",
    "A perfectly good idea acquired three unnecessary features.",
    "The AI Council has been summoned for reasons nobody can explain.",
    "A README was rewritten instead of fixing the actual bug.",
    "GitHub received another commit. Nobody knows why. Not even GitHub.",
    "The project now has lore. This was not in the specification.",
    "Someone said 'tiny project' and immediately lied.",
]

VERDICTS = [
    "ABSOLUTELY TMG",
    "Questionably productive",
    "Feature creep detected",
    "AI Council intervention recommended",
    "This is becoming a whole thing",
    "Ship it. Future TMG can deal with it.",
]


def main() -> None:
    chaos = random.randint(1, 100)
    event = random.choice(TMG_EVENTS)
    verdict = random.choice(VERDICTS)

    print("=== TMG CHAOS ENGINE ===")
    print(f"Chaos: {chaos}/100")
    print(f"Verdict: {verdict}")
    print(f"Event: {event}")

    if chaos >= 90:
        print("STATUS: THE COUNCIL HAS LOST CONTROL")
    elif chaos >= 60:
        print("STATUS: This is no longer a small project")
    else:
        print("STATUS: Somehow still under control")


if __name__ == "__main__":
    main()
