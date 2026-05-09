# Agent Guidance

This section explains how coding agents should use this repository.

## Agent workflow

1. Read `AGENTS.md`.
2. Use `docs/index.md` to find the right knowledge area.
3. Follow spec-driven workflows in `docs-specs/`.
4. Use `scripts/generate_pg_docs.py` to capture database evidence.

## Safe-change guidance

- Do not modify generated schema docs without re-running the generator.
- Prefer linking rather than rewriting existing docs.
- Mark uncertainty explicitly.
