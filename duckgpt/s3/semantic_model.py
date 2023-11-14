import json

from duckgpt.s3.tables import tables, relationships


def get_semantic_model() -> str:
    """Returns the semantic model of the s3 data warehouse as a string"""

    sematic_model = {
        "tables": [table.model_dump(exclude_none=True) for table in tables],
        "relationships": [relationship.model_dump(exclude_none=True) for relationship in relationships],
    }
    return json.dumps(sematic_model, indent=4)
