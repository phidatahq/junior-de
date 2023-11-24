import pandas as pd
import numpy as np

# Function to load movie data
def load_movie_data(filepath):
    return pd.read_csv(filepath)

# Function to analyze movie ratings and decide on bucket size
def calculate_bucket_size(ratings):
    range_of_ratings = ratings.max() - ratings.min()
    # Sturges' rule can be a good starting point for choosing number of bins
    num_bins = int(np.ceil(np.log2(len(ratings)) + 1))
    bucket_size = round(range_of_ratings / num_bins, 2)
    return bucket_size, num_bins

# Function to calculate histogram data of movies by rating
def get_histogram_data(data, num_bins):
    min_rating = data['Rating'].min()
    max_rating = data['Rating'].max()
    bins = np.linspace(min_rating, max_rating, num_bins + 1)
    histogram_data = pd.cut(data['Rating'], bins=bins, include_lowest=True).value_counts().sort_index()
    return histogram_data.to_dict()

# Main function to load data and calculate histogram data
if __name__ == "__main__":
    histogram_data = {}
    movie_data = load_movie_data('/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv')
    bucket_size, num_bins = calculate_bucket_size(movie_data['Rating'])
    histogram_data = get_histogram_data(movie_data, num_bins)