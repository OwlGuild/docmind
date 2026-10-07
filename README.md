# docmind

Vector search and retrieval-augmented generation over documents, built on PostgreSQL
`pgvector`. Part of the [OwlGuild](https://github.com/OwlGuild) family.

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-16-336791.svg)](https://www.postgresql.org/)
[![pgvector](https://img.shields.io/badge/vector-pgvector-4d4d4d.svg)](https://github.com/pgvector/pgvector)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

## Why this exists

Keyword search finds the word you used. It does not find the idea you meant. DocMind keeps
everything inside PostgreSQL — no separate vector database to run, back up or pay for — and
answers questions with the passages that actually support the answer, each with a citation.

## How it works

```
document
  → chunk on paragraph boundaries (not fixed token windows)
  → embed each chunk
  → store alongside the original text in PostgreSQL
  → query: embed the question, nearest-neighbour search
  → rank, then return passages with their source offsets
```

`pgvector` handles similarity search with an HNSW index. Nothing leaves the database.

## Stack

| Layer | Choice |
|---|---|
| Runtime | Python 3.12 |
| Database | PostgreSQL 16 + `pgvector` |
| Embeddings | pluggable provider behind one interface |
| API | Django REST Framework |
| Queue | Celery for bulk ingestion |
| Container | Docker + docker-compose |

## Quickstart

```bash
git clone https://github.com/OwlGuild/docmind.git
cd docmind
cp .env.example .env
docker compose up --build
docker compose exec api python manage.py migrate
docker compose exec api python manage.py ingest /path/to/docs
```

## API

| Method | Path | Description |
|---|---|---|
| `POST` | `/documents/` | upload a document for ingestion |
| `GET` | `/documents/{id}/` | ingestion status and chunk count |
| `POST` | `/search/` | nearest-neighbour search, returns ranked passages |
| `POST` | `/ask/` | question → passages → answer with citations |

## Design notes

- **Chunking follows paragraphs.** Fixed windows split sentences and hurt recall.
- **Embedding provider is an interface.** Swapping models changes one class, not the schema.
- **Metadata is queryable.** Source, author and section filter results before ranking.
- **The index is rebuilt offline.** Ingestion never blocks reads.

## Testing

```bash
docker compose exec api pytest
```

Nearest-neighbour tests use a seeded corpus with known answers, so a regression in recall fails
the build rather than shipping quietly.

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