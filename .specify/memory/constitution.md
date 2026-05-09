# Documentation Constitution

## Purpose

Create and maintain agent-readable documentation for a multi-repo enterprise application.

## Non-Negotiable Principles

1. Do not invent undocumented systems, APIs, tables, queues, topics, fields, or business rules.
2. Every important claim must be based on repository evidence, schema files, config files, migrations, sample data, tests, or existing docs.
3. If evidence is incomplete, write `Unknown` or `Needs confirmation`.
4. Prefer small indexed Markdown files over one large document.
5. Give every repo, database, queue, topic, API, business flow, and How-To a stable ID.
6. Business flows must link to repos, databases, APIs, and message channels.
7. Agent guidance must include safe-change rules and testing expectations.
8. Generated docs must be useful to Claude, Copilot, and future coding agents.
