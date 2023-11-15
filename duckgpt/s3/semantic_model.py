import json

from duckgpt.s3.tables import s3_tables, s3_table_relationships


def get_semantic_model() -> str:
    """Returns the semantic model of the s3 data warehouse as a string"""

    sematic_model = {
        "tables": [table.model_dump(exclude_none=True) for table in s3_tables],
        "relationships": [
            relationship.model_dump(exclude_none=True) for relationship in s3_table_relationships
        ],
    }
    return json.dumps(sematic_model, indent=4)
