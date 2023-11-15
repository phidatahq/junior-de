from typing import List

import streamlit as st
from phi.conversation import Conversation

from app.openai_key import get_openai_key
from app.password import check_password
from app.reload import reload_button
from app.user_name import get_user_name
from duckgpt.s3.conversation import duckdb_s3_agent, get_duckgpt_s3_conversation
from duckgpt.s3.load_tables import load_s3_tables
from utils.log import logger


st.title(":snowman: DuckGPT")
st.markdown('<a href="https://github.com/phidatahq/phidata"><h4>by phidata</h4></a>', unsafe_allow_html=True)


def restart_conversation():
    st.session_state["s3_conversation"] = None
    st.session_state["s3_conversation_id"] = None
    st.rerun()


def main() -> None:
    # Get users OpenAI API key
    get_openai_key()

    # Get user name
    user_name = get_user_name()
    if user_name:
        st.sidebar.info(f":technologist: User: {user_name}")
    else:
        st.write(":technologist: Please enter a username")
        return

    # Get the conversation
    s3_conversation: Conversation
    if "s3_conversation" not in st.session_state or st.session_state["s3_conversation"] is None:
        logger.info("---*--- Creating DuckGPT Conversation ---*---")
        s3_conversation = get_duckgpt_s3_conversation(
            user_name=user_name,
            debug_mode=True,
        )
        st.session_state["s3_conversation"] = s3_conversation
    else:
        s3_conversation = st.session_state["s3_conversation"]

    # Start conversation and save conversation id in session state
    st.session_state["s3_conversation_id"] = s3_conversation.start()

    # Load messages for existing conversation
    user_chat_history = s3_conversation.memory.get_chat_history()
    if len(user_chat_history) > 0:
        logger.debug("Loading chat history")
        st.session_state["messages"] = user_chat_history
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
            response = ""
            resp_container = st.empty()
            for delta in s3_conversation.chat(question):
                response += delta
                resp_container.markdown(response)

            st.session_state["messages"].append({"role": "assistant", "content": response})

    if st.sidebar.button("New Conversation"):
        restart_conversation()

    if st.sidebar.button("Load Tables"):
        alert = st.sidebar.info("Loading data...", icon="ℹ️")
        load_s3_tables(duckdb_agent=duckdb_s3_agent)
        st.sidebar.success("Tables loaded")
        alert.empty()

    if st.sidebar.button("Auto Rename"):
        s3_conversation.auto_rename()

    if s3_conversation.storage:
        all_pdf_conversation_ids: List[str] = s3_conversation.storage.get_all_conversation_ids(
            user_name=user_name
        )
        new_pdf_conversation_id = st.sidebar.selectbox("Conversation ID", options=all_pdf_conversation_ids)
        if st.session_state["s3_conversation_id"] != new_pdf_conversation_id:
            logger.debug(f"Loading conversation {new_pdf_conversation_id}")
            logger.info("---*--- Loading DuckGPT Conversation ---*---")
            st.session_state["s3_conversation"] = get_duckgpt_s3_conversation(
                user_name=user_name,
                conversation_id=new_pdf_conversation_id,
                debug_mode=True,
            )
            st.rerun()

    s3_conversation_name = s3_conversation.name
    if s3_conversation_name:
        st.sidebar.write(f":thread: {s3_conversation_name}")

    # Show reload button
    reload_button()


if check_password():
    main()
