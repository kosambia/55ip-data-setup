---
id: doc-messaging-index
type: index
description: "Messaging and Events index"
---
# Messaging Index

Index of all Kafka topics and message queues.

## Topics

### `trade-execution-events`
- **Producer**: `55ip-trade`
- **Consumer**: `external-broker-gateway`
- **Description**: Emits trade orders generated after tax-loss harvesting execution.

### `portfolio-updates`
- **Producer**: `55ip-portfolio`
- **Consumer**: `55ip-tax`, `55ip-client`
- **Description**: Emitted when a portfolio's holdings change.
