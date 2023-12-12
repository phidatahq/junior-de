from typing import List
from pydantic import BaseModel

from phi.tools.duckdb import DuckDbTools

from utils.log import logger


class S3Table(BaseModel):
    name: str
    columns: List[str]
    description: str
    path: str


class Relationship(BaseModel):
    name: str
    type: str
    keys: List[str]
    description: str


s3_tables = [
    S3Table(
        name="titles",
        columns=[
            "tconst",
            "titleType",
            "primaryTitle",
            "originalTitle",
            "isAdult",
            "startYear",
            "endYear",
            "runtimeMinutes",
            "genres",
        ],
        description="Contains information about movie and TV show titles.",
        path="s3://phi-public/imdb/titles.parquet",
    ),
    S3Table(
        name="name",
        columns=[
            "nconst",
            "primaryName",
            "birthYear",
            "deathYear",
            "knownForTitles",
        ],
        description="Contains information about cast and crew names.",
        path="s3://phi-public/imdb/name.parquet",
    ),
    S3Table(
        name="ratings",
        columns=[
            "tconst",
            "averageRating",
            "numVotes",
        ],
        description="Contains ratings for movies and TV shows.",
        path="s3://phi-public/imdb/ratings.parquet",
    ),
    S3Table(
        name="principals",
        columns=[
            "tconst",
            "ordering",
            "nconst",
            "category",
            "job",
            "characters",
        ],
        description="Contains information about the main players (actors, directors, writers, etc.) for each title.",
        path="s3://phi-public/imdb/principals.parquet",
    ),
    S3Table(
        name="episode",
        columns=[
            "tconst",
            "parentTconst",
            "seasonNumber",
            "episodeNumber",
        ],
        description="Contains information about TV episode details and their parent show.",
        path="s3://phi-public/imdb/episode.parquet",
    ),
]

s3_table_relationships = [
    Relationship(
        name="title-principals",
        type="One-to-Many",
        keys=["tconst (in Titles)", "tconst (in Principals)"],
        description="Links titles to their main players, including actors, directors, and other key roles.",
    ),
    Relationship(
        name="principals-name",
        type="One-to-One",
        keys=["nconst (in Principals)", "nconst (in Names)"],
        description="Represents the association of cast and crew with movie and TV show titles.",
    ),
    Relationship(
        name="title-rating",
        type="One-to-One",
        keys=["tconst (in Titles)", "tconst (in Ratings)"],
        description="Represents the rating information for each title.",
    ),
    Relationship(
        name="title-episode",
        type="One-to-Many",
        keys=["tconst (in Titles)", "parentTconst (in Episode)"],
        description="Links episodes to their parent TV show title.",
    ),
]


def load_s3_tables(duckdb_tools: DuckDbTools) -> None:
    """Load S3 tables to DuckDB"""

    for table in s3_tables:
        duckdb_tools.create_table_from_path(path=table.path, table=table.name)
        logger.info(f"Created table: {table.name}")
