import json

from duckgpt.local_tables import local_tables
from duckgpt.s3_tables import s3_tables, s3_table_relationships


def get_local_semantic_model() -> str:
    """Returns the semantic model of the local data warehouse as a string"""

    sematic_model = {
        "tables": [table.model_dump(exclude_none=True) for table in local_tables],
    }
    return json.dumps(sematic_model, indent=4)


def get_s3_semantic_model() -> str:
    """Returns the semantic model of the s3 data warehouse as a string"""

    sematic_model = {
        "tables": [table.model_dump(exclude_none=True) for table in s3_tables],
        "relationships": [
            relationship.model_dump(exclude_none=True) for relationship in s3_table_relationships
        ],
    }
    return json.dumps(sematic_model, indent=4)
