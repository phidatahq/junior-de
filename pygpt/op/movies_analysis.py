import pandas as pd
import streamlit as st

# Load data
@st.cache
def load_data():
    return pd.read_csv('/usr/local/app/data/imdb/Movies.csv')

# Number of Movies Released Per Year
def movies_per_year(df):
    return df['Year'].value_counts().sort_index()

# Movie Ratings Distribution
def ratings_distribution(df):
    return df['Rating'].apply(lambda x: int(x)).value_counts().sort_index()

# Revenue Over the Years
def revenue_over_years(df):
    return df.groupby('Year')['Revenue_Millions'].sum()

if __name__ == '__main__':
    df = load_data()
    
    # Chart 1: Number of Movies Released Per Year
    movies_year = movies_per_year(df)
    st.bar_chart(movies_year)
    
    # Chart 2: Movie Ratings Distribution
    ratings_dist = ratings_distribution(df)
    st.bar_chart(ratings_dist)
    
    # Chart 3: Revenue Over the Years
    revenue_years = revenue_over_years(df)
    st.line_chart(revenue_years)