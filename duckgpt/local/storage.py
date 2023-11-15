from phi.conversation.storage.postgres import PgConversationStorage

from duckgpt.db import db_settings

duckgpt_local_storage = PgConversationStorage(
    table_name="duckgpt_local_conversations",
    db_url=db_settings.get_db_url(),
    schema="llm",
)
