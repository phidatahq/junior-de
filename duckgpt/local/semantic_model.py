import json

from duckgpt.local.tables import tables


def get_semantic_model() -> str:
    """Returns the semantic model of the local data warehouse as a string"""

    sematic_model = {
        "tables": [table.model_dump(exclude_none=True) for table in tables],
    }
    return json.dumps(sematic_model, indent=4)
