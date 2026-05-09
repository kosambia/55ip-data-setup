# Generated Data Documentation

This directory is intended to contain generated PostgreSQL table docs.

Each table should have a generated Markdown file with:
- YAML front matter including stable ID and source
- column definitions
- primary key information
- sample rows
- notes and business meaning

Run `python3 scripts/generate_pg_docs.py` to populate this directory from an accessible PostgreSQL database.
