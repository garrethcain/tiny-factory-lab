# Development

## Requirements

- [uv](https://docs.astral.sh/uv/)
- Python 3.12 (uv will provision it)

## Setup

```
make sync
make migrate
make run
```

The API is then at http://127.0.0.1:8000/api/ (browsable DRF UI included).

## Quality gates

Every PR must pass:

```
make check
```

which runs:

- `uv run ruff check .`
- `uv run ruff format --check .`
- `uv run mypy src`
- `uv run pytest -q`

## Endpoints

- `GET /api/healthz/` - liveness probe
- `GET|POST /api/devices/` - device registry
- `GET /api/devices/{id}/` - device detail
