from phi.tools.duckdb import DuckDbTools

duckdb_local_tools = DuckDbTools()
duckdb_s3_tools = DuckDbTools(init_commands=["SET s3_region='us-east-1';"])
