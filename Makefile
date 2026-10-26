.PHONY: test lint format check new

test:
	uv run pytest -q

lint:
	uv run ruff check .

format:
	uv run ruff format .
	uv run ruff check --select I --fix .

check:
	uv run ruff check .
	uv run ruff format --check .
	uv run pytest -q

new:
	@uv run python scripts/new_problem.py $(path)
