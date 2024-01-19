from phi.knowledge.json import JSONKnowledgeBase
from phi.knowledge.text import TextKnowledgeBase
from phi.knowledge.combined import CombinedKnowledgeBase
from phi.vectordb.pgvector import PgVector

from db.session import db_url
from workspace.settings import ws_settings

duckgpt_text_knowledge_base = TextKnowledgeBase(
    path=ws_settings.ws_root.joinpath("ai", "duckgpt", "knowledge"),
    formats=[".txt", ".sql"],
)

duckgpt_json_knowledge_base = JSONKnowledgeBase(
    path=ws_settings.ws_root.joinpath("ai", "duckgpt", "knowledge"),
)

duckgpt_knowledge_base = CombinedKnowledgeBase(
    sources=[
        duckgpt_text_knowledge_base,
        duckgpt_json_knowledge_base,
    ],
    # Store this knowledge base in ai.duckgpt_knowledge
    vector_db=PgVector(
        schema="ai",
        db_url=db_url,
        collection="duckgpt_knowledge",
    ),
    # 5 references are added to the prompt
    num_documents=5,
)

pygpt_text_knowledge_base = TextKnowledgeBase(
    path=ws_settings.ws_root.joinpath("ai", "pygpt", "knowledge"),
    formats=[".txt"],
)

pygpt_json_knowledge_base = JSONKnowledgeBase(
    path=ws_settings.ws_root.joinpath("ai", "pygpt", "knowledge"),
)

pygpt_knowledge_base = CombinedKnowledgeBase(
    sources=[
        pygpt_text_knowledge_base,
        pygpt_json_knowledge_base,
    ],
    # Store this knowledge base in ai.pygpt_knowledge
    vector_db=PgVector(
        schema="ai",
        db_url=db_url,
        collection="pygpt_knowledge",
    ),
    # 5 references are added to the prompt
    num_documents=5,
)
