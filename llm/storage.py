from phi.storage.conversation.postgres import PgConversationStorage

from llm.db import db_settings

duckgpt_local_storage = PgConversationStorage(
    table_name="duckgpt_local_conversations",
    db_url=db_settings.get_db_url(),
    schema="llm",
)

duckgpt_s3_storage = PgConversationStorage(
    table_name="duckgpt_s3_conversations",
    db_url=db_settings.get_db_url(),
    schema="llm",
)

pygpt_storage = PgConversationStorage(
    table_name="pygpt_conversations",
    db_url=db_settings.get_db_url(),
    schema="llm",
)
