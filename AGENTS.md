# AGENTS.md

Start here before editing or extending this repository.

## Required reading

1. `README.md`
2. `docs/index.md`
3. `.specify/memory/constitution.md`
4. `docs-specs/001-system-inventory/spec.md`
5. `docs-specs/002-repo-index/spec.md`
6. `docs-specs/003-business-flows/spec.md`

## Purpose

This file provides a high-level route for agents. It does not duplicate the full documentation.

## Safe-change rules

- Do not invent systems, tables, APIs, flows, or contracts.
- Always base claims on evidence from source code, DB schema, config, or existing documentation.
- If evidence is incomplete, write `Unknown` or `Needs confirmation`.
- Do not modify generated schema documentation without validating against the database.
- When changing business flows, update the related spec and task files.

## Entry points

- `docs/index.md` — top-level navigation
- `docs/data/index.md` — database and schema docs
- `docs/business-flows/index.md` — flow inventory
- `docs/architecture/index.md` — architecture and system inventory
- `.github/copilot-instructions.md` — Copilot-specific guidance
