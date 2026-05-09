---
id: db-table-positions
type: database-schema
description: "Schema for positions table"
owner: data-engineering-team
database: portfolio
---
# Positions Table

## `positions` Table
Tracks the current holdings and quantities for each account and strategy.

### Schema
- `position_id` (BIGSERIAL, PK)
- `account_id` (BIGINT, FK -> `account.account_id`, ON DELETE CASCADE)
- `strategy_id` (BIGINT, FK -> `model_strategy.strategy_id`)
- `symbol` (TEXT, NOT NULL)
- `cusip` (TEXT)
- `asset_class` (TEXT, NOT NULL) - IN ('US_EQUITY', 'INTL_EQUITY', 'FIXED_INCOME', 'ETF', 'MUNICIPAL_BOND')
- `quantity` (NUMERIC(18,6), >= 0)
- `target_weight` (NUMERIC(9,6), 0 to 1)
- `current_price` (NUMERIC(18,4), > 0)
- `market_value` (NUMERIC(18,2), >= 0)
- `unrealized_gain_loss` (NUMERIC(18,2), Default 0)
- `as_of_date` (DATE)
- `created_at` (TIMESTAMPTZ)

**Constraints**: `(account_id, symbol)` must be unique.
