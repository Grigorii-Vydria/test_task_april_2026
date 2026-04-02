#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
CLOUD_INIT_PATH = ROOT / "cloud-init" / "runner-cloud-init.yaml"
API = "https://api.hetzner.cloud/v1"


def env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


def main() -> int:
    token = env("HCLOUD_TOKEN")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    name = os.getenv("RUNNER_NAME", "self-improvement-runner")
    payload = {
        "name": name,
        "server_type": os.getenv("HCLOUD_SERVER_TYPE", "cx22"),
        "image": os.getenv("HCLOUD_IMAGE", "ubuntu-24.04"),
        "location": os.getenv("HCLOUD_LOCATION", "nbg1"),
        "user_data": CLOUD_INIT_PATH.read_text(),
        "labels": {"project": "self-improvement", "ephemeral": "true"},
        # NOTE: attach firewall/network IDs here if you pre-create them.
    }
    response = requests.post(f"{API}/servers", headers=headers, data=json.dumps(payload), timeout=60)
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
