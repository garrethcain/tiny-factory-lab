# Architecture

- Django 5 + Django REST Framework, Python 3.12, managed with `uv`
- SQLite for local persistence
- API routes live under `/api/` and contain no business logic
- Business logic belongs in `src/app/services/`
- Serializers are the API boundary; models are the storage boundary
- Tests use pytest + pytest-django against an ephemeral test database

## Layout

```
src/
  manage.py
  config/       settings, root URLconf, WSGI/ASGI
  app/          models, serializers, views, urls, migrations, services/
tests/          pytest suite
```

## Non-goals

- Authentication
- Pagination
- Background workers / Celery
- Cloud deployment
- Docker
- MQTT integration
- Django admin site
