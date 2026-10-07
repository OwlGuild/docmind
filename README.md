# docmind

Vector search and retrieval-augmented generation over documents, built on PostgreSQL
`pgvector`. Part of the [OwlGuild](https://github.com/OwlGuild) family.

[![CI](https://github.com/OwlGuild/docmind/actions/workflows/ci.yml/badge.svg)](https://github.com/OwlGuild/docmind/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-5.0-092E20.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-16-336791.svg)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

## Why this exists

Keyword search finds the word you used. It does not find the idea you meant. DocMind keeps
everything inside PostgreSQL — no separate vector database to run, back up or pay for — and
returns the passages that actually support the answer, each with a citation.

## How it works

```
document
  → chunk on paragraph boundaries (not fixed token windows)
  → embed each chunk
  → store alongside the original text in PostgreSQL
  → query: embed the question, nearest-neighbour search
  → rank, then return passages with their source offsets
```

## Stack

| Layer | Choice |
|---|---|
| Runtime | Python 3.12 |
| Framework | Django 5 + Django REST Framework |
| Database | PostgreSQL 16 (SQLite for tests) |
| Search | `pgvector` with an HNSW index |
| Container | Docker |

## Quickstart

```bash
git clone https://github.com/OwlGuild/docmind.git
cd docmind
pip install -r requirements.txt
python manage.py runserver
curl http://localhost:8000/health/
# {"status": "ok", "service": "docmind"}
```

## API

| Method | Path | Description |
|---|---|---|
| `GET` | `/health/` | liveness probe used by CI and uptime checks |

## Testing

```bash
pip install -r requirements.txt
pytest -q
# 3 passed
```

The suite covers the health contract: status code, payload shape and routing. CI runs it on
every push against Python 3.12.

## Roadmap

- Paragraph-boundary chunker with a seeded recall corpus
- Pluggable embedding provider behind a single interface
- `pgvector` schema, HNSW index and migrations
- `POST /documents/`, `POST /search/` and `POST /ask/` endpoints
- Celery queue for bulk ingestion

## Design notes

- **Chunking follows paragraphs.** Fixed windows split sentences and hurt recall.
- **Embedding provider is an interface.** Swapping models changes one class, not the schema.
- **Metadata is queryable.** Source, author and section filter results before ranking.
- **The index is rebuilt offline.** Ingestion never blocks reads.

## Ownership

Both maintainers of [OwlGuild](https://github.com/OwlGuild) commit here.

| Area | Maintainer |
|---|---|
| Embeddings, search, ranking | [@MarziehAkrami](https://github.com/MarziehAkrami) |
| Schema, `pgvector` index, migrations | [@MarziehAkrami](https://github.com/MarziehAkrami) |
| Ingestion queue and API | [@MarziehAkrami](https://github.com/MarziehAkrami) |
| Consumer UI | [@AhmadGolbooee](https://github.com/AhmadGolbooee) |
| CI, Docker, docs | shared |

## License

[MIT](LICENSE).
