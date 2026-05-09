---
id: db-table-account
type: database-schema
description: "Schema for account and account_number_registry tables"
owner: data-engineering-team
database: portfolio
---
# Account Tables

## `account` Table
The primary table storing client accounts, linking them to households and model strategies.

### Schema
- `account_id` (BIGSERIAL, PK)
- `account_number` (TEXT, NOT NULL)
- `household_id` (TEXT, NOT NULL)
- `client_name` (TEXT, NOT NULL)
- `registration_type` (TEXT, NOT NULL) - IN ('TAXABLE', 'IRA', 'JOINT', 'TRUST')
- `base_currency` (CHAR(3), NOT NULL) - Default 'USD'
- `tax_status` (TEXT, NOT NULL) - IN ('TAXABLE', 'TAX_DEFERRED', 'TAX_EXEMPT')
- `account_open_date` (DATE, NOT NULL)
- `model_strategy_id` (BIGINT, FK -> `model_strategy.strategy_id`)
- `market_value` (NUMERIC(18,2))
- `cash_balance` (NUMERIC(18,2))
- `created_at` (TIMESTAMPTZ)

## `account_number_registry` Table
A simple registry ensuring unique global account numbers. Maintained via a PostgreSQL trigger (`trg_sync_account_number_registry`) on the `account` table.

### Schema
- `account_number` (TEXT, PK)
