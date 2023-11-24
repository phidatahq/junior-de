from duckgpt.s3_tables import load_s3_tables
from llm.agents.duckdb_agent import duckdb_s3_agent

load_s3_tables(duckdb_agent=duckdb_s3_agent)
