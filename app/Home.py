import streamlit as st

from phi.tools.streamlit.components import check_password

st.set_page_config(
    page_title="Data Engineering AI",
    page_icon=":orange_heart:",
)
st.title("Junior Data Engineer")
st.markdown("##### :orange_heart: built using [phidata](https://github.com/phidatahq/phidata)")


def main() -> None:
    st.markdown("---")
    st.markdown("### Select your Junior Data Engineer:")
    st.markdown("#### 1. PyGPT: Data analysis using Python")
    st.markdown("#### 2. DuckGPT: Answer data questions using DuckDB")

    st.sidebar.success("Select App from above")


if check_password():
    main()
