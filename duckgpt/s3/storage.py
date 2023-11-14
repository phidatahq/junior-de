from phi.conversation.storage.postgres import PgConversationStorage

from duckgpt.db import db_settings

duckgpt_storage = PgConversationStorage(
    table_name="s3_duckgpt_conversations",
    db_url=db_settings.get_db_url(),
    schema="llm",
)
