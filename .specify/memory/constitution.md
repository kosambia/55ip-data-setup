---
id: doc-constitution
type: standards
description: "Core rules for agents interacting with this repo"
---
# Documentation Constitution

1. **Never duplicate knowledge.** Link to it.
2. **Every Markdown file must have YAML front matter.** This includes `id`, `type`, and `description`.
3. **Use stable IDs.** Do not change an `id` once established.
4. **Mark unknowns.** If you (the agent) are unsure about a producer/consumer or table owner, mark it as `Unknown` or `Needs confirmation`.
5. **Always update the indexes.** If you add a module, update `docs/repos/index.md`. If you add a table, update `docs/data/index.md`.
