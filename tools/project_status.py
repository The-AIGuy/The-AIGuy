#!/usr/bin/env python3
"""Show a simple, human-readable status card for the TMG project ecosystem."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    tools = sorted((ROOT / "tools").glob("*.py"))
    print("TMG PROJECT STATUS")
    print("==================")
    print(f"Repository: {ROOT.name}")
    print(f"Tools: {len(tools)}")
    for tool in tools:
        print(f"  - {tool.name}")
    print()
    print("Community: Slack #tmg-hangout")
    print("Experiments: Slack #tmg-chaos-lab")
    print("Source of truth: GitHub")
    print("Status: building, experimenting, and trying to keep this understandable")


if __name__ == "__main__":
    main()
