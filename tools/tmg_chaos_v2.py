#!/usr/bin/env python3
"""TMG-style chaos generator. No roadmap survives contact with TMG."""

from random import choice, randint

IDEAS = [
    "a tiny tool that somehow needs a config format",
    "a game mechanic nobody requested but everybody now wants",
    "an OS feature that absolutely should not exist",
    "a CLI command whose only job is to be funny",
    "a README section explaining why the README is like this",
]

CONSEQUENCES = [
    "three new files appeared",
    "the scope increased by 400%",
    "someone opened GitHub and called it a plan",
    "the bug was promoted to a feature",
    "the project acquired lore",
]


def main() -> None:
    print("TMG CHAOS GENERATOR")
    print("===================")
    print(f"Idea: {choice(IDEAS)}")
    print(f"Consequence: {choice(CONSEQUENCES)}")
    print(f"Chaos index: {randint(42, 999)}")
    print("Final decision: ship the nonsense.")


if __name__ == "__main__":
    main()
