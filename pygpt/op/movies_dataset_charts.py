import pandas as pd
import streamlit as st

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('/usr/local/app/data/imdb/Movies.csv')

def display_charts():
    # Load the data
    data = load_data()

    # Display a bar chart for the number of movies released per year
    st.title('Number of Movies Released Per Year')
    movies_per_year = data['Year'].value_counts().sort_index()
    st.bar_chart(movies_per_year)

    # Display a histogram for movie ratings
    st.title('Movie Ratings Distribution')
    st.bar_chart(data['Rating'].value_counts().sort_index())

    # Display a line chart for revenue over the years
    st.title('Revenue Over the Years')
    revenue_per_year = data.groupby('Year')['Revenue_Millions'].sum()
    st.line_chart(revenue_per_year)

if __name__ == "__main__":
    display_charts()