from typing import List, Optional
from pydantic import BaseModel

from phi.tools.duckdb import DuckDbTools

from workspace.settings import ws_settings
from utils.log import logger


class LocalTable(BaseModel):
    name: str
    columns: Optional[List[str]] = None
    description: str
    path: str


local_tables = [
    LocalTable(
        name="movies",
        columns=[
            "Rank",
            "Title",
            "Genre",
            "Description",
            "Director",
            "Actors",
            "Year",
            "Runtime_Minutes",
            "Rating",
            "Votes",
            "Revenue_Millions",
            "Metascore",
        ],
        description="Contains information about movies from IMDB.",
        path=str(ws_settings.ws_root.joinpath("data/imdb/Movies.csv")),
    ),
]


def load_local_tables(duckdb_tools: DuckDbTools):
    """Load local tables to DuckDB"""

    for table in local_tables:
        duckdb_tools.create_table_from_path(path=table.path, table=table.name)
        logger.info(f"Created table: {table.name}")
