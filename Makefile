PYTHON ?= python3
VENV ?= .venv

.PHONY: venv install test lint format validate bootstrap

venv:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip

install: venv
	$(VENV)/bin/pip install -e .[dev]

test:
	$(VENV)/bin/pytest -q

lint:
	$(VENV)/bin/ruff check .

format:
	$(VENV)/bin/ruff format .

validate: lint test

bootstrap:
	bash scripts/bootstrap.sh
