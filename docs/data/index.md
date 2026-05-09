# Data Documentation

This section documents PostgreSQL database schema and table metadata.

## How to generate

Use the PostgreSQL introspection script:

```bash
python3 scripts/generate_pg_docs.py
```

## Current status

- No schema docs have been generated in this repository yet.
- The generator will create one Markdown file per discovered table and an updated index.

## Generated output

- `docs/data/index.md`
- `docs/data/generated/<schema>.<table>.md`

## Notes

- The generator is designed to use DB evidence rather than manual guesses.
- It will include column definitions, primary key information, and sample rows.
