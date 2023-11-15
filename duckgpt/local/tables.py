from typing import List, Optional
from pydantic import BaseModel

from workspace.settings import ws_settings


class LocalTable(BaseModel):
    name: str
    columns: Optional[List[str]] = None
    description: str
    path: str


local_tables = [
    LocalTable(
        name="Movies",
        description="Contains information about movies rom IMDB.",
        path=str(ws_settings.ws_root.joinpath("data/imdb/Movies.csv")),
    ),
]
