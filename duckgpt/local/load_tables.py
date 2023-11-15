from phi.agent.duckdb import DuckDbAgent

from duckgpt.local.tables import local_tables
from utils.log import logger


def load_local_tables(duckdb_agent: DuckDbAgent):
    """Load local tables to DuckDB"""

    for table in local_tables:
        duckdb_agent.load_local_path_to_table(path=table.path, table=table.name)
        logger.info(f"Loaded table: {table.name}")
