import streamlit as st

from phi.tools.streamlit.components import check_password

st.set_page_config(
    page_title="Data Engineering AI",
    page_icon=":snowman:",
)

st.title(":snowman: Junior Data Engineer AI")
st.markdown('<a href="https://github.com/phidatahq/phidata"><h4>by phidata</h4></a>', unsafe_allow_html=True)


def main() -> None:
    st.markdown("### Select your Junior Data Engineer:")
    st.markdown("#### 1. DuckGPT: Answer data questions using DuckDB")
    st.markdown("#### 2. PyGPT: Accomplish any task using Python")

    st.sidebar.success("Select App from above")


if check_password():
    main()
