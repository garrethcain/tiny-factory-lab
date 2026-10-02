# tiny-factory-lab

A tiny software factory for learning how the
issue -> agent -> PR -> CI -> review loop works, built on
[Django](https://www.djangoproject.com/) + [DRF](https://www.django-rest-framework.org/),
[uv](https://docs.astral.sh/uv/), [OpenCode](https://opencode.ai) and
GitHub Actions.

The "product" is a deliberately boring sensor-reading API. The real subject
of study is the factory that builds it. See
[docs/FACTORY.md](docs/FACTORY.md) for the operating manual.

## Quickstart

```
make sync
make migrate
make check
make run
```

## The loop

1. Open an issue using the Feature template.
2. Triage it until it has concrete acceptance criteria.
3. Label it `ready-for-agent` (or implement it yourself - Phase 1).
4. The agent opens `agent/issue-N` with a PR; CI gates it; the review agent
   posts findings; you merge.
