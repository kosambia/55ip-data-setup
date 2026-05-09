---
spec_id: DOC-SPEC-001
title: Generate documentation from repository evidence
owner: documentation
status: draft
output_root: docs/
---

# Goal

Generate documentation for an enterprise application using source evidence, database metadata, and architectural guidance.

# Inputs

- code repositories
- config files
- database schema metadata
- sample rows
- APIs, OpenAPI, AsyncAPI
- existing README files

# Required Outputs

- docs/index.md
- docs/system-overview.md
- docs/architecture/index.md
- docs/data/index.md
- docs/business-flows/index.md

# Rules

- Do not invent facts.
- Mark uncertain evidence as `Unknown` or `Needs confirmation`.
- Use relative links between docs.
- Keep documents concise and indexed by stable IDs.
