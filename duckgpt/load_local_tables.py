from duckgpt.local_tables import load_local_tables
from llm.tools.duckdb_tools import duckdb_local_tools

load_local_tables(duckdb_tools=duckdb_local_tools)
