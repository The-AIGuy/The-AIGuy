#!/usr/bin/env python3
"""TMG Collab Seed: a tiny shared idea board for the Chaos Lab.

Run it with Python to get a random starting point for a collaborative build.
The point is not to predict the project. The point is to give humans something
small enough to actually build together before the scope mutates into folklore.
"""

from random import choice


SEEDS = [
    "Build a tiny CLI that solves one annoying problem in a ridiculous way.",
    "Turn a boring developer workflow into a tiny game.",
    "Make a tool that explains one confusing programming concept interactively.",
    "Build a micro-game that can be completed in under five minutes.",
    "Create a useful automation script with one completely unnecessary feature.",
    "Make a tiny diagnostic tool that reports problems with unnecessarily dramatic wording.",
]

CONSTRAINTS = [
    "Keep it under 150 lines.",
    "Use only the Python standard library.",
    "Make the output readable in a terminal.",
    "Give it at least one easter egg.",
    "Document the idea in the README before adding complexity.",
]


def generate_seed() -> tuple[str, str]:
    """Return a random collaboration prompt and constraint."""
    return choice(SEEDS), choice(CONSTRAINTS)


def main() -> None:
    idea, constraint = generate_seed()
    print("TMG COLLAB SEED")
    print("===============")
    print(f"Build: {idea}")
    print(f"Constraint: {constraint}")
    print("Collaboration rule: improve the idea before expanding the scope.")
    print("Final rule: if the bug is funny, document it before calling it a feature.")


if __name__ == "__main__":
    main()
