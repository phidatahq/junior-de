import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to load movie data
def load_movie_data(filepath):
    return pd.read_csv(filepath)

# Function to analyze movie ratings and decide on bucket size
def calculate_bucket_size(ratings):
    range_of_ratings = ratings.max() - ratings.min()
    # Sturges' rule can be a good starting point for choosing number of bins
    num_bins = int(np.ceil(np.log2(len(ratings)) + 1))
    bucket_size = round(range_of_ratings / num_bins, 2)
    return bucket_size

# Function to create a histogram of movies by rating
def generate_histogram(data, bucket_size):
    plt.hist(data['Rating'], bins=np.arange(data['Rating'].min(), data['Rating'].max() + bucket_size, bucket_size))
    plt.title('Histogram of Movies by Rating')
    plt.xlabel('Rating')
    plt.ylabel('Number of Movies')
    plt.show()

# Main function to load data and create histogram
if __name__ == "__main__":
    movie_data = load_movie_data('/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv')
    bucket_size = calculate_bucket_size(movie_data['Rating'])
    generate_histogram(movie_data, bucket_size)