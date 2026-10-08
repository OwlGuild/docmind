# Contributing

Part of [OwlGuild](https://github.com/OwlGuild).

## Ground rules

- Small pull requests; one concern per commit.
- English commit messages in the imperative mood ("Add readiness probe").
- Behaviour changes ship with a test that fails before the fix.
- CI must be green before review.

## Local checks

```bash
pip install -r requirements.txt
cp .env.example .env
python manage.py check
DEBUG=false python manage.py check --deploy --fail-level WARNING
pytest -q
```

CI runs the same suite against PostgreSQL 16 with `pgvector`, so a green local run on SQLite
is necessary but not sufficient for database-related changes.

## Review

Both maintainers review before merge. Keep discussion in the PR, keep scope in the diff.
