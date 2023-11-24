from typing import List, Optional
from pydantic import BaseModel

from workspace.settings import ws_settings


class CsvFile(BaseModel):
    name: str
    columns: Optional[List[str]] = None
    description: str
    path: str


csv_files = [
    CsvFile(
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
