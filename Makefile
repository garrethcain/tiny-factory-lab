.PHONY: sync format lint test check migrate run

sync:
	uv sync

format:
	uv run ruff format .

lint:
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy src

test:
	uv run pytest -q

check: lint test

migrate:
	uv run python src/manage.py migrate

run:
	uv run python src/manage.py runserver
