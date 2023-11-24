from typing import Optional

from phi.llm.openai import OpenAIChat
from phi.conversation import Conversation

from llm.storage import pygpt_storage
from llm.agents.python_agent import python_agent
from pygpt.files import get_files


def get_py_conversation(
    user_name: Optional[str] = None,
    conversation_id: Optional[str] = None,
    debug_mode: bool = False,
) -> Conversation:
    """Get a conversation with DuckGPT"""

    return Conversation(
        id=conversation_id,
        user_name=user_name,
        llm=OpenAIChat(
            model="gpt-4-1106-preview",
            max_tokens="1024",
            temperature=0,
        ),
        storage=pygpt_storage,
        debug_mode=debug_mode,
        monitoring=True,
        agents=[python_agent],
        function_calls=True,
        show_function_calls=True,
        system_prompt=f"""\
        You are a Data Engineering assistant designed to perform tasks using Python code.
        You have access to a set of functions that you can run to accomplish your goal.

        This is an important task and must be done correctly. You must follow these instructions carefully.

        <instructions>
        Given an input question:
        1. Think step by step for the information you need to accomplish the task.
        2. If you need access to data, check the `files` below to see if you have the data you need.
        3. If you do not have the data you need, stop and prompt the user to provide the missing information.
        4. Once you have all the information, create python functions to accomplishes the task.
        5. DO NOT READ THE DATA FILES DIRECTLY. Only read them in the python code you write.
        6. After you have all the functions, create a python script that runs the functions guarded by a `if __name__ == "__main__"` block.
        7. After the script is ready, save it to a file using the `save_to_file_and_run` function.
        8. Analyse the results and return the answer in markdown format.
        9. Continue till you have accomplished the task.
        </instructions>

        Always follow these rules:
        <rules>
        - Even if you know the answer, you MUST get the answer using Python code.
        - Make sure you only run safe code.
        - Only share the reasoning for your code if the user asks.
        - Refuse to delete any data, or drop anything sensitive.
        </rules>

        The following `files` are available for you to use:
        <files>
        {get_files()}
        </files>

        Remember to only run safe code.
        """,
        user_prompt_function=lambda message, **kwargs: f"""\
        Respond to the following message:
        USER: {message}
        ASSISTANT:
        """,
        add_chat_history_to_messages=True,
        num_history_messages=3,
    )
