from duckgpt.local_tables import load_local_tables
from llm.agents.duckdb_agent import duckdb_local_agent

load_local_tables(duckdb_agent=duckdb_local_agent)
