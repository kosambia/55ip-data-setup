# CLAUDE.md

This repository is an agent-readable documentation scaffold.

## What to do first

1. Read `AGENTS.md`.
2. Read `docs/index.md`.
3. Read `.specify/memory/constitution.md`.
4. Use the spec files in `docs-specs/` to understand what documentation should be generated.

## High-level guidance

- Keep generated docs concise and evidence-based.
- Use YAML front matter for stable IDs and metadata.
- Prefer linking to existing docs rather than duplicating content.
- When inspecting the database, use `scripts/generate_pg_docs.py` and do not hardcode schema details.
