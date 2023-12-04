import pandas as pd
import streamlit as st

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('/usr/local/app/data/imdb/Movies.csv')

# Number of movies released per year
def movies_per_year():
    df = load_data()
    movies_count = df.groupby('Year')['Title'].count().reset_index()
    movies_count.columns = ['Year', 'Number of Movies']
    return movies_count

# Movie ratings distribution
def ratings_distribution():
    df = load_data()
    ratings = df.groupby('Rating').size().reset_index(name='Count')
    return ratings

# Revenue over the years
def revenue_over_years():
    df = load_data()
    revenue = df.groupby('Year')['Revenue_Millions'].sum().reset_index()
    return revenue

if __name__ == '__main__':
    st.title('Movie Dataset Analysis')

    st.header('1. Number of Movies Released Per Year')
    movies_count = movies_per_year()
    st.bar_chart(movies_count.set_index('Year'))

    st.header('2. Movie Ratings Distribution')
    ratings = ratings_distribution()
    st.bar_chart(ratings.set_index('Rating'))

    st.header('3. Revenue Over the Years')
    revenue = revenue_over_years()
    st.line_chart(revenue.set_index('Year'))