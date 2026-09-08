"""The AI Chaos Meter

A tiny, harmless CLI toy for measuring how catastrophically chaotic a project idea is.
"""

from __future__ import annotations

import random


EVENTS = [
    "Copilot suggested upgrading to Windows 2.0.",
    "Someone opened Reversi instead of fixing the bug.",
    "The build passed on the first try. Suspicious.",
    "A README gained three more exclamation marks.",
    "An AI confidently invented a feature that does not exist.",
    "Git status is clean. Civilization may yet survive.",
]


def chaos_level() -> int:
    """Return a random chaos score from 0 to 100."""
    return random.randint(0, 100)


def main() -> None:
    score = chaos_level()
    if score < 25:
        verdict = "Suspiciously calm"
    elif score < 50:
        verdict = "Manageable nonsense"
    elif score < 75:
        verdict = "Considerably chaotic"
    else:
        verdict = "THE AI COUNCIL HAS ESCAPED"

    print(f"Chaos score: {score}/100")
    print(f"Verdict: {verdict}")
    print(f"Random event: {random.choice(EVENTS)}")


if __name__ == "__main__":
    main()
