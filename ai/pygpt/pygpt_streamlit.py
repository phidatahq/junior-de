from typing import Optional

from phi.assistant.python import PythonAssistant
from phi.llm.openai import OpenAIChat

from ai.settings import ai_settings
from ai.storage import pygpt_storage
from ai.knowledge_base import pygpt_knowledge_base
from workspace.settings import ws_settings


def get_pygpt(
    run_id: Optional[str] = None,
    user_id: Optional[str] = None,
    debug_mode: bool = False,
) -> PythonAssistant:
    """Returns a PythonAssistant with a knowledge base."""

    return PythonAssistant(
        name="pygpt",
        run_id=run_id,
        user_id=user_id,
        llm=OpenAIChat(
            model=ai_settings.gpt_4,
            max_tokens=ai_settings.default_max_tokens,
            temperature=ai_settings.default_temperature,
        ),
        storage=pygpt_storage,
        knowledge_base=pygpt_knowledge_base,
        monitoring=True,
        use_tools=True,
        show_tool_calls=True,
        followups=True,
        charting_libraries=["streamlit"],
        debug_mode=debug_mode,
        base_dir=ws_settings.ws_root.joinpath("ai", "pygpt", "scratch"),
        # Provide information about the files the python assistant can access in the prompt
        # file_information=ws_settings.ws_root.joinpath("ai", "pygpt", "knowledge", "files.json").read_text(),
    )
