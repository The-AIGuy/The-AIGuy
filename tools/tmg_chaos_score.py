#!/usr/bin/env python3
"""Calculate a silly but repeatable chaos score for a project description."""

import sys


def score(text: str) -> int:
    words = text.lower().split()
    triggers = {
        "ai": 80,
        "feature": 55,
        "integration": 90,
        "automation": 75,
        "game": 45,
        "os": 100,
        "lore": 60,
        "slack": 85,
        "github": 85,
        "canva": 70,
    }
    total = 42
    for word in words:
        total += triggers.get(word.strip(".,!?;:"), 7)
    return min(total, 999)


def main() -> None:
    text = " ".join(sys.argv[1:]).strip()
    if not text:
        text = "tiny TMG project"
    value = score(text)
    if value < 200:
        verdict = "contained nonsense"
    elif value < 500:
        verdict = "serious feature creep"
    elif value < 800:
        verdict = "the roadmap is becoming sentient"
    else:
        verdict = "TMG CHAOS EVENT: SHIP THE NONSENSE"
    print(f"Chaos score: {value}/999")
    print(f"Verdict: {verdict}")


if __name__ == "__main__":
    main()
