from phi.storage.assistant.postgres import PgAssistantStorage

from db.session import db_url

duckgpt_storage = PgAssistantStorage(
    schema="ai",
    db_url=db_url,
    table_name="duckgpt",
)

pygpt_storage = PgAssistantStorage(
    schema="ai",
    db_url=db_url,
    table_name="pygpt",
)
