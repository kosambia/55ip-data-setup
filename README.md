# 55ip-data-setup

This repository is a documentation scaffold built from the Agent-Readable Documentation and Knowledge Graph Plan.

It includes:
- an agent-friendly documentation structure
- spec-driven workflows for generating docs
- a PostgreSQL schema documentation generator
- a reference document inspired by Apache Fineract

## Getting started

1. Install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

2. Point the generator at your PostgreSQL database:

```bash
export PGHOST=localhost
export PGPORT=5432
export PGDATABASE=postgres
export PGUSER=postgres
export PGPASSWORD=password
python3 scripts/generate_pg_docs.py
```

3. Review the generated documentation in `docs/`.

## Purpose

This repo is intentionally lightweight and agent-readable. It is designed to let coding agents and engineers discover:
- system inventory
- repo and flow documentation
- database schema knowledge
- messaging contracts
- agent onboarding guidance

## How this repo uses the plan

The repository structure is built from the DOCX plan located at `/home/kosambia/Downloads/agent_readable_documentation_kg_plan.docx`.
The generated doc files follow the same spec-driven workflow described there.
