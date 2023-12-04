import streamlit as st
import pandas as pd

# Function to read the movies data
def read_movies_data(csv_path):
    return pd.read_csv(csv_path)

# Function to plot the number of movies released per year
def plot_movies_per_year(data):
    movies_per_year = data['Year'].value_counts().sort_index()
    st.subheader('Number of Movies Released Per Year')
    st.bar_chart(movies_per_year)

# Function to plot the movie ratings distribution
def plot_ratings_distribution(data):
    ratings_distribution = data['Rating'].value_counts(bins=10, sort=False).sort_index()
    st.subheader('Movie Ratings Distribution')
    st.bar_chart(ratings_distribution)

# Function to plot revenue over the years
def plot_revenue_over_years(data):
    revenue_per_year = data.groupby('Year')['Revenue_Millions'].sum()
    st.subheader('Revenue Over the Years')
    st.line_chart(revenue_per_year)

if __name__ == "__main__":
    # Path to the movies CSV file
    csv_file_path = '/usr/local/app/data/imdb/Movies.csv'

    # Read movies data
    movies_data = read_movies_data(csv_file_path)

    # Plot the charts
    plot_movies_per_year(movies_data)
    plot_ratings_distribution(movies_data)
    plot_revenue_over_years(movies_data)