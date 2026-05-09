---
id: db-table-model-strategy
type: database-schema
description: "Schema for model_strategy table"
owner: quant-team
database: portfolio
---
# Model Strategy Table

## `model_strategy` Table
Defines the tax-aware investment strategies that can be assigned to client accounts.

### Schema
- `strategy_id` (BIGSERIAL, PK)
- `strategy_code` (TEXT, NOT NULL, UNIQUE)
- `strategy_name` (TEXT, NOT NULL)
- `risk_profile` (TEXT, NOT NULL) - IN ('Conservative', 'Moderate', 'Growth', 'Aggressive')
- `benchmark_code` (TEXT, NOT NULL)
- `rebalance_frequency` (TEXT, NOT NULL) - IN ('MONTHLY', 'QUARTERLY', 'THRESHOLD')
- `is_tax_aware` (BOOLEAN, NOT NULL) - Default TRUE
- `created_at` (TIMESTAMPTZ)
