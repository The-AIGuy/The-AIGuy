#!/usr/bin/env python3
"""TMG Chaos Protocol: turn ordinary project events into harmless nonsense."""

from random import choice, randint

EVENTS = [
    "a feature request escaped the issue tracker",
    "the README developed opinions",
    "a tiny fix became a subsystem",
    "someone renamed a variable and accidentally created lore",
    "the roadmap was last seen running toward the horizon",
    "a perfectly normal commit started acting suspicious",
]

RESPONSES = [
    "promote it to a feature",
    "open another terminal and pretend this is intentional",
    "document the incident immediately",
    "add it to the lore archive",
    "ship it before the universe notices",
    "declare victory and make a backup",
]


def run() -> None:
    event = choice(EVENTS)
    response = choice(RESPONSES)
    chaos = randint(1, 1000)
    print("TMG CHAOS PROTOCOL")
    print("==================")
    print(f"Incident: {event}")
    print(f"Recommended response: {response}")
    print(f"Chaos index: {chaos}/1000")
    print("Council status: debating whether this counts as a feature")
    print("Final decision: SHIP THE NONSENSE")


if __name__ == "__main__":
    run()
