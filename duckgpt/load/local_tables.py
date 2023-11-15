from duckgpt.local.conversation import duckdb_local_agent
from duckgpt.local.load_tables import load_local_tables

load_local_tables(duckdb_agent=duckdb_local_agent)
