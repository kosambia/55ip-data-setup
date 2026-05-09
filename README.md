# 55ip Data Setup Repository

Welcome to the 55ip Data Setup project. This repository is modeled after a modular architecture to support the data pipelines, tax rules, portfolio setups, and client configurations for the automated tax-smart investment platform.

It is fully configured with an **Agent-Readable Documentation Knowledge Graph** to ensure autonomous coding assistants (like Claude or GitHub Copilot) can safely navigate and modify the system.

## File Structure

```text
55ip-data-setup/
├── .github/
│   └── copilot-instructions.md
├── .specify/
│   └── memory/
│       └── constitution.md
├── 55ip-client/         # Client profiles and advisor logic 
├── 55ip-core/           # Shared logic across the platform 
├── 55ip-db/             # DB migrations and setup 
├── 55ip-portfolio/      # Account holdings and portfolio logic 
├── 55ip-tax/            # Tax harvesting and cost basis algorithms 
├── 55ip-trade/          # Trade generation and execution 
├── docs/
│   ├── index.md                  # Root documentation index
│   ├── repos/
│   │   └── index.md              # Index of active code repos
│   ├── messaging/
│   │   └── index.md              # Kafka/Event topics documentation
│   ├── data/
│   │   ├── index.md              # Database summary and table index
│   │   ├── table-account.md      # account schema
│   │   ├── table-model-strategy.md # model_strategy schema
│   │   ├── table-orders.md       # orders schema
│   │   ├── table-positions.md    # positions schema
│   │   ├── table-tax-lot.md      # tax_lot schema
│   │   └── table-trades.md       # trades schema
│   └── specs/
│       ├── DOC-SPEC-001.md
│       ├── DOC-SPEC-002.md
│       └── DOC-SPEC-003.md
├── AGENTS.md            # Entry point for autonomous coding agents
└── CLAUDE.md            # Anthropic Claude-specific instructions
```

## Getting Started
Please begin by reading `AGENTS.md` and `docs/index.md` before making any changes.
