#!/usr/bin/env python3
"""Tiny local helper for TMG Hangout collaboration.

This is intentionally not a real Slack integration. It is a dependency-free
prototype that generates friendly prompts for welcoming new builders and
starting small collaborations.
"""

from random import choice

WELCOME = [
    "Welcome to TMG Hangout! What are you building lately?",
    "New builder detected. What are you experimenting with?",
    "Welcome! Bring an idea, a half-finished project, or a gloriously strange bug.",
]

PROMPTS = [
    "Take a tiny project and add one feature you would actually use.",
    "Find one annoying problem and build the smallest possible tool for it.",
    "Pair up with someone and turn one random idea into a working prototype.",
    "Take a boring CLI and give it one unnecessarily delightful feature.",
]

RESPONSES = [
    "TMG BOT: project scope detected. Proceed carefully.",
    "TMG BOT: that idea has potential. Someone should probably build it.",
    "TMG BOT: collaboration opportunity detected.",
    "TMG BOT: bug accepted as temporary lore.",
]


def main() -> None:
    print("TMG HANGOUT BOT // LOCAL PROTOTYPE")
    print("==================================")
    print(f"Welcome: {choice(WELCOME)}")
    print(f"Challenge: {choice(PROMPTS)}")
    print(f"Bot response: {choice(RESPONSES)}")
    print("Status: ready for humans to improve.")


if __name__ == "__main__":
    main()
