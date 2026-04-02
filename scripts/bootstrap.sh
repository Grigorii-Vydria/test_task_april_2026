#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "Created .env from .env.example"
else
  echo ".env already exists"
fi

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]

echo
echo "Next steps:"
echo "1. Fill in .env"
echo "2. Add matching GitHub Actions secrets"
echo "3. Run: source .venv/bin/activate && bash scripts/run_validation.sh"
