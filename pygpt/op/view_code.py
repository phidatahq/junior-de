import streamlit as st

def show_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    st.code(code)

if __name__ == '__main__':
    code_path = 'streamlit_charts.py'  # The file path to the code we want to show
    show_code(code_path)