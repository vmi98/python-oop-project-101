install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=validator --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build