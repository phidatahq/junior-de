from duckgpt.s3.conversation import duckdb_s3_agent
from duckgpt.s3.load_tables import load_s3_tables

load_s3_tables(duckdb_agent=duckdb_s3_agent)
