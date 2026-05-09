---
id: db-table-tax-lot
type: database-schema
description: "Schema for tax_lot and trade_tax_lot_application tables"
owner: quant-team
database: portfolio
---
# Tax Lot Tables

## `tax_lot` Table
Critical table for tax-smart investing. Tracks individual lots of securities for cost basis, holding periods, and wash sale rules.

### Schema
- `tax_lot_id` (BIGINT, IDENTITY, PK composite with position_id)
- `position_id` (BIGINT, FK -> `positions`, PK composite)
- `account_id` (BIGINT, FK -> `account`)
- `opening_trade_id` (BIGINT, FK -> `trades`)
- `symbol` (TEXT, NOT NULL)
- `lot_open_date` (DATE, NOT NULL)
- `quantity` (NUMERIC(18,6), > 0)
- `remaining_quantity` (NUMERIC(18,6))
- `cost_basis_price` (NUMERIC(18,4), > 0)
- `current_price` (NUMERIC(18,4))
- `cost_basis_amount` (NUMERIC(18,2))
- `market_value` (NUMERIC(18,2))
- `unrealized_gain_loss` (NUMERIC(18,2))
- `gain_loss_type` (TEXT) - IN ('LONG', 'SHORT')
- `holding_period_days` (INTEGER)
- `wash_sale_restricted` (BOOLEAN, Default FALSE)

## `trade_tax_lot_application` Table
Mapping table that specifies exactly which tax lots were relieved (sold) by a specific sell trade.

### Schema
- `trade_id` (BIGINT, FK -> `trades`)
- `position_id` (BIGINT)
- `tax_lot_id` (BIGINT)
- `applied_quantity` (NUMERIC(18,6), > 0)

**Composite Primary Key:** `(trade_id, position_id, tax_lot_id)`
**Foreign Key:** `(position_id, tax_lot_id) -> tax_lot(position_id, tax_lot_id)`
