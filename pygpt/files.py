import json

from pygpt.csv_files import csv_files


def get_files() -> str:
    """Returns the files for pygpt as a string"""

    files = {
        "csv_files": [c.model_dump(exclude_none=True) for c in csv_files],
    }
    return json.dumps(files, indent=4)
