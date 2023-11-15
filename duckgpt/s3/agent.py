from phi.agent.duckdb import DuckDbAgent

from workspace.settings import ws_settings

duckdb_s3_db = ws_settings.ws_root.joinpath("storage/s3.db")
duckdb_s3_agent = DuckDbAgent(db_path=str(duckdb_s3_db), init_commands=["SET s3_region='us-east-1';"])
