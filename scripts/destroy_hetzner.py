#!/usr/bin/env python3
from __future__ import annotations

import os
import sys

import requests

API = "https://api.hetzner.cloud/v1"


def env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


def main() -> int:
    token = env("HCLOUD_TOKEN")
    server_id = env("HCLOUD_SERVER_ID")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{API}/servers/{server_id}", headers=headers, timeout=60)
    response.raise_for_status()
    print(f"Deleted Hetzner server {server_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
