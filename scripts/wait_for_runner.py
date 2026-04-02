#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
import time

import requests


def env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


def main() -> int:
    repo = env("GITHUB_REPOSITORY")
    token = env("GH_PAT")
    runner_name = env("RUNNER_NAME")
    timeout_seconds = int(os.getenv("RUNNER_WAIT_TIMEOUT", "600"))
    deadline = time.time() + timeout_seconds
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    url = f"https://api.github.com/repos/{repo}/actions/runners"
    while time.time() < deadline:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        runners = response.json().get("runners", [])
        for runner in runners:
            if runner["name"] == runner_name and runner["status"] == "online":
                print(f"Runner {runner_name} is online")
                return 0
        time.sleep(10)
    raise SystemExit(f"Runner {runner_name} did not come online in time")


if __name__ == "__main__":
    sys.exit(main())
