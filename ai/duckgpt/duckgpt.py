from typing import Optional

from phi.assistant.duckdb import DuckDbAssistant
from phi.llm.openai import OpenAIChat

from ai.settings import ai_settings
from ai.storage import duckgpt_storage
from ai.knowledge_base import duckgpt_knowledge_base
from workspace.settings import ws_settings  # noqa: F401


def get_duckgpt(
    run_id: Optional[str] = None,
    user_id: Optional[str] = None,
    debug_mode: bool = True,
) -> DuckDbAssistant:
    """Returns a DuckDbAssistant with a knowledge base."""

    return DuckDbAssistant(
        name="duckgpt",
        run_id=run_id,
        user_id=user_id,
        llm=OpenAIChat(
            model=ai_settings.gpt_4,
            max_tokens=ai_settings.default_max_tokens,
            temperature=ai_settings.default_temperature,
        ),
        storage=duckgpt_storage,
        knowledge_base=duckgpt_knowledge_base,
        update_knowledge_base=True,
        followups=True,
        monitoring=True,
        use_tools=True,
        show_tool_calls=True,
        debug_mode=debug_mode,
        # Provide information about the tables the data assistant can access in the prompt
        # semantic_model=ws_settings.ws_root.joinpath("ai", "duckgpt", "knowledge", "tables.json").read_text(),
    )
