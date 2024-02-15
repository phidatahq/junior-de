from typing import List

import streamlit as st
from phi.assistant.duckdb import DuckDbAssistant
from phi.tools.streamlit.components import (
    get_openai_key_sidebar,
    check_password,
    reload_button_sidebar,
    get_username_sidebar,
)

from ai.duckgpt.duckgpt import get_duckgpt
from utils.log import logger

st.set_page_config(
    page_title="DuckGPT",
    page_icon=":orange_heart:",
)
st.title("DuckGPT")
st.markdown("##### :orange_heart: built using [phidata](https://github.com/phidatahq/phidata)")
with st.expander(":rainbow[:point_down: Ask questions like]"):
    st.markdown("- Give me a histogram of movies by rating")
    st.markdown("- Show me the revenue over time")
    st.markdown("- Who is the most popular actor")


def restart_assistant():
    st.session_state["duckgpt"] = None
    st.session_state["duckgpt_run_id"] = None
    st.session_state["file_uploader_key"] += 1
    st.rerun()


def main() -> None:
    # Get OpenAI key from environment variable or user input
    get_openai_key_sidebar()

    # Get username
    username = get_username_sidebar()
    if username:
        st.sidebar.info(f":technologist: User: {username}")
    else:
        st.markdown("---")
        st.markdown("#### :technologist: Enter a username and start chatting")
        return

    # Get the assistant
    duckgpt: DuckDbAssistant
    if "duckgpt" not in st.session_state or st.session_state["duckgpt"] is None:
        logger.info("---*--- Creating DuckGPT ---*---")
        duckgpt = get_duckgpt(
            user_id=username,
            debug_mode=True,
        )
        st.session_state["duckgpt"] = duckgpt
    else:
        duckgpt = st.session_state["duckgpt"]

    # Create assistant run (i.e. log to database) and save run_id in session state
    st.session_state["duckgpt_run_id"] = duckgpt.create_run()

    # Check if knowlege base exists
    if duckgpt.knowledge_base and (
        "duckgpt_kb_loaded" not in st.session_state or not st.session_state["duckgpt_kb_loaded"]
    ):
        if not duckgpt.knowledge_base.exists():
            logger.info("Knowledge base does not exist")
            loading_container = st.sidebar.info("🧠 Loading knowledge base")
            duckgpt.knowledge_base.load()
            st.session_state["duckgpt_kb_loaded"] = True
            st.sidebar.success("Knowledge base loaded")
            loading_container.empty()

    # Load messages for existing assistant
    assistant_chat_history = duckgpt.memory.get_chat_history()
    if len(assistant_chat_history) > 0:
        logger.debug("Loading chat history")
        st.session_state["messages"] = assistant_chat_history
    else:
        logger.debug("No chat history found")
        st.session_state["messages"] = [{"role": "assistant", "content": "Ask me anything..."}]

    # Prompt for user input
    if prompt := st.chat_input():
        st.session_state["messages"].append({"role": "user", "content": prompt})

    # Display existing chat messages
    for message in st.session_state["messages"]:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is from a user, generate a new response
    last_message = st.session_state["messages"][-1]
    if last_message.get("role") == "user":
        question = last_message["content"]
        with st.chat_message("assistant"):
            with st.spinner("Working..."):
                response = ""
                resp_container = st.empty()
                for delta in duckgpt.run(question):
                    response += delta  # type: ignore
                    resp_container.markdown(response)

            st.session_state["messages"].append({"role": "assistant", "content": response})

    if st.sidebar.button("New Run"):
        restart_assistant()

    if duckgpt.knowledge_base:
        if st.sidebar.button("Update Knowledge Base"):
            duckgpt.knowledge_base.load(recreate=False)
            st.session_state["duckgpt_kb_loaded"] = True
            st.sidebar.success("Knowledge base updated")

        if st.sidebar.button("Recreate Knowledge Base"):
            duckgpt.knowledge_base.load(recreate=True)
            st.session_state["duckgpt_kb_loaded"] = True
            st.sidebar.success("Knowledge base recreated")

    if st.sidebar.button("Auto Rename"):
        duckgpt.auto_rename_run()

    if duckgpt.storage:
        all_duckgpt_run_ids: List[str] = duckgpt.storage.get_all_run_ids(user_id=username)
        new_duckgpt_run_id = st.sidebar.selectbox("Run ID", options=all_duckgpt_run_ids)
        if st.session_state["duckgpt_run_id"] != new_duckgpt_run_id:
            logger.debug(f"Loading run {new_duckgpt_run_id}")
            logger.info("---*--- Loading DuckGPT Run ---*---")
            st.session_state["duckgpt"] = get_duckgpt(
                user_id=username,
                run_id=new_duckgpt_run_id,
                debug_mode=True,
            )
            st.rerun()

    duckgpt_run_name = duckgpt.run_name
    if duckgpt_run_name:
        st.sidebar.write(f":thread: {duckgpt_run_name}")

    # Show reload button
    reload_button_sidebar()


if check_password():
    main()
