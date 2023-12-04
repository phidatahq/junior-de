import streamlit as st

from app.password import check_password

st.set_page_config(
    page_title="DE LLM",
    page_icon=":snowman:",
)

st.title(":snowman: Junior Data Engineer")
st.markdown('<a href="https://github.com/phidatahq/phidata"><h4>by phidata</h4></a>', unsafe_allow_html=True)


def main() -> None:
    st.markdown("### Select your Junior Data Engineer:")
    st.markdown("#### 1. PyGPT: Automate data analysis with Python")
    st.markdown("#### 2. DuckGPT Local: Query local data with DuckDB")
    st.markdown("#### 3. DuckGPT S3: Query data in S3 with DuckDB")
    st.sidebar.success("Select App from above")


if check_password():
    main()
