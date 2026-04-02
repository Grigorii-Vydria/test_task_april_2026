#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TARGETS = ["README.md", "ARCHITECTURE.md", "SECURITY.md", "COST.md", "tests", "src"]


def repo_snapshot() -> dict:
    files = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and ".git" not in path.parts and ".venv" not in path.parts:
            rel = path.relative_to(ROOT)
            files.append(str(rel))
    return {
        "allowed_targets": ALLOWED_TARGETS,
        "files": files,
        "max_changed_files": int(os.getenv("SELF_IMPROVEMENT_MAX_CHANGED_FILES", "5")),
        "max_changed_lines": int(os.getenv("SELF_IMPROVEMENT_MAX_CHANGED_LINES", "120")),
    }


def main() -> int:
    model = os.getenv("OPENAI_MODEL", "gpt-5.4")
    snapshot = repo_snapshot()
    out = ROOT / "artifacts"
    out.mkdir(exist_ok=True)
    (out / "self-improvement-plan.json").write_text(json.dumps({"model": model, **snapshot}, indent=2))
    print("Prepared self-improvement snapshot.")
    print("This scaffold intentionally does not auto-call the LLM without credentials + prompt contract.")
    print("Expected next step: wire OpenAI call, generate a tiny diff, run validation, open PR.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
