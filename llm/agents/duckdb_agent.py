from phi.agent.duckdb import DuckDbAgent

duckdb_local_agent = DuckDbAgent()
duckdb_s3_agent = DuckDbAgent(init_commands=["SET s3_region='us-east-1';"])
