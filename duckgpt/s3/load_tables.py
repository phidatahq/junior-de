from phi.agent.duckdb import DuckDbAgent

from duckgpt.s3.tables import tables
from utils.log import logger


def load_tables(duckdb_agent: DuckDbAgent) -> None:
    """Load S3 tables to DuckDB"""

    for table in tables:
        duckdb_agent.load_s3_path_to_table(path=table.path, table=table.name)
        logger.info(f"Loaded table: {table.name}")
