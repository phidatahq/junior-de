from phi.conversation.storage.postgres import PgConversationStorage

from duckgpt.db import db_settings

duckgpt_s3_storage = PgConversationStorage(
    table_name="duckgpt_s3_conversations",
    db_url=db_settings.get_db_url(),
    schema="llm",
)
