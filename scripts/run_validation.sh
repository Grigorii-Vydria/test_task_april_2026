#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip >/dev/null
pip install -e .[dev] >/dev/null
ruff check .
pytest -q
