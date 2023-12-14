from duckgpt.s3_tables import load_s3_tables
from llm.tools.duckdb_tools import duckdb_s3_tools

load_s3_tables(duckdb_tools=duckdb_s3_tools)
