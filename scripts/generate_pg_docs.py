#!/usr/bin/env python3
"""Generate PostgreSQL schema documentation into docs/data/generated."""

import os
import sys
from pathlib import Path

try:
    import psycopg2
except ImportError:
    print("Missing dependency: psycopg2-binary. Install with 'pip install -r requirements.txt'.")
    sys.exit(1)

OUTPUT_ROOT = Path(__file__).resolve().parent.parent / "docs" / "data" / "generated"
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

DB_PARAMS = {
    "host": os.getenv("PGHOST", "localhost"),
    "port": os.getenv("PGPORT", "5432"),
    "dbname": os.getenv("PGDATABASE", "postgres"),
    "user": os.getenv("PGUSER", os.getenv("USER")),
    "password": os.getenv("PGPASSWORD", ""),
}

SCHEMA_FILTER = os.getenv("PGSCHEMA", "public")


def connect():
    return psycopg2.connect(**{k: v for k, v in DB_PARAMS.items() if v})


def query(conn, sql, params=None):
    with conn.cursor() as cur:
        cur.execute(sql, params or ())
        return cur.fetchall()


def format_table_doc(schema, table, columns, primary_keys, sample_rows):
    lines = [
        f"---",
        f"id: DATA-{schema.upper()}-{table.upper()}",
        f"type: Table",
        f"schema: {schema}",
        f"table: {table}",
        f"source: PostgreSQL",
        f"---",
        "",
        f"# {schema}.{table}",
        "",
        "## Purpose",
        "Document the table schema and example rows for agent-assisted investigation.",
        "",
        "## Columns",
        "",
        "| Column | Type | Nullable | Default | Description |",
        "|---|---|---|---|---|",
    ]
    for col in columns:
        name, data_type, is_nullable, column_default = col
        lines.append(
            f"| {name} | {data_type} | {is_nullable} | {column_default or ''} | Unknown |"
        )
    lines.append("")
    if primary_keys:
        lines.append("## Primary key")
        lines.append("")
        lines.append(", ".join(primary_keys))
        lines.append("")
    if sample_rows:
        lines.append("## Sample rows")
        lines.append("")
        headers = [col[0] for col in columns]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        for row in sample_rows:
            values = [str(v) if v is not None else "NULL" for v in row]
            lines.append("| " + " | ".join(values) + " |")
        lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Data purpose: Unknown")
    lines.append("- Confirm business meaning from application code or product owners.")
    return "\n".join(lines)


def write_index(database, table_docs):
    index_path = Path(__file__).resolve().parent.parent / "docs" / "data" / "index.md"
    lines = [
        "# Data Documentation",
        "",
        f"Generated from PostgreSQL database `{database}`.",
        "",
        "## Table index",
        "",
    ]
    for schema, tables in table_docs.items():
        lines.append(f"### Schema: {schema}")
        lines.append("")
        for table in tables:
            doc_path = f"generated/{schema}.{table}.md"
            lines.append(f"- [{schema}.{table}]({doc_path})")
        lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Documentation is generated from database introspection.")
    lines.append("- Each table document should be reviewed and enriched with business meaning.")
    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {index_path}")


def main():
    conn = connect()
    database = DB_PARAMS["dbname"]
    print(f"Connected to PostgreSQL database: {database}")

    tables = query(
        conn,
        """
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE'
          AND table_schema NOT IN ('pg_catalog', 'information_schema')
          AND table_schema LIKE %s
        ORDER BY table_schema, table_name
        """,
        (SCHEMA_FILTER,),
    )

    if not tables:
        print("No tables found.")
        return

    table_docs = {}
    for schema, table in tables:
        columns = query(
            conn,
            """
            SELECT column_name, data_type, is_nullable, column_default
            FROM information_schema.columns
            WHERE table_schema = %s
              AND table_name = %s
            ORDER BY ordinal_position
            """,
            (schema, table),
        )
        pkeys = query(
            conn,
            """
            SELECT a.attname
            FROM pg_index i
            JOIN pg_attribute a ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
            WHERE i.indrelid = %s::regclass
              AND i.indisprimary
            ORDER BY a.attnum
            """,
            (f"{schema}.{table}",),
        )
        sample_rows = query(
            conn,
            f"SELECT * FROM {schema}.\"{table}\" LIMIT 3",
        )
        table_docs.setdefault(schema, []).append(table)
        doc_text = format_table_doc(schema, table, columns, [pk[0] for pk in pkeys], sample_rows)
        doc_path = OUTPUT_ROOT / f"{schema}.{table}.md"
        doc_path.write_text(doc_text, encoding="utf-8")
        print(f"Wrote {doc_path}")

    write_index(database, table_docs)
    print("Completed generation.")


if __name__ == "__main__":
    main()
