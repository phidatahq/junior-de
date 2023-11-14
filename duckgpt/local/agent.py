from phi.agent.duckdb import DuckDbAgent

from workspace.settings import ws_settings

duckdb_database = ws_settings.ws_root.joinpath("storage/local.db")
duckdb_agent = DuckDbAgent(db_path=str(duckdb_database))
