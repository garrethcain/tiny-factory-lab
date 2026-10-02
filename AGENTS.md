# Agent rules

## Scope

- Work only on the GitHub issue linked in the task.
- Do not perform unrelated refactors.
- Do not modify GitHub Actions, dependency definitions in `pyproject.toml`,
  deployment files, secrets configuration, or CI policy unless the issue
  explicitly requires it.

## Engineering

- Python 3.12, Django + Django REST Framework, managed with `uv`.
- Quality gates (all must pass): `uv run ruff check .`,
  `uv run ruff format --check .`, `uv run mypy src`, `uv run pytest -q`.
  Equivalent shortcut: `make check`.
- Add or update tests for every observable behaviour introduced or changed.
- Commit Django migrations with the change that requires them
  (`uv run python src/manage.py makemigrations`). Never edit an applied migration.
- Routes contain no business logic; put logic in `src/app/services/`.
- Keep dependencies minimal; justify any new runtime dependency in the PR.

## Git

- Never push to `main`.
- Commit your work on the current branch provided by the automation.
- Do not create, rename, or delete branches yourself; branch and pull
  request handling is owned by the harness.
- Create exactly one commit series and one pull request per issue.
- The PR description must include: issue link, approach, commands run with
  results, and known limitations.

## Safety

- Never print, commit, or transmit secrets.
- Do not use external services or credentials. This project has no production.
- If acceptance criteria conflict, are incomplete, or require forbidden
  changes, stop and comment on the issue with specific questions instead of
  opening a speculative PR.
