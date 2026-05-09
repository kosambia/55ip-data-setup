# System Overview

This repository contains an agent-oriented documentation scaffold for a multi-repository enterprise application.

## Purpose

The objective is to make the application easier for coding agents and engineers to understand by creating:
- indexed knowledge nodes
- spec-driven docs
- safe-change guidance
- evidence-based schema and flow documentation

## Current state

- The repository is currently a documentation scaffold.
- Database metadata is intended to be loaded from a PostgreSQL instance using `scripts/generate_pg_docs.py`.
- The structure follows the recommendation from the agent-readable documentation plan.

## Fineract reference

This documentation model is informed by Apache Fineract, which is a financially-oriented enterprise platform with a modular architecture, API-first design, database-driven data model, and strong operational documentation.

For more details, see [Fineract reference](reference/fineract.md).
