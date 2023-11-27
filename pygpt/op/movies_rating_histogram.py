import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# function to load movie data
def load_movie_data(file_path):
    return pd.read_csv(file_path)

# function to determine bucket size for histogram
def determine_bucket_size(data_series):
    range_of_data = data_series.max() - data_series.min()
    number_of_buckets = np.ceil(np.sqrt(len(data_series)))
    bucket_size = range_of_data / number_of_buckets
    return bucket_size, number_of_buckets

# function to plot histogram
def plot_histogram(data, bucket_size, number_of_buckets):
    plt.figure(figsize=(10,6))
    plt.hist(data, bins=int(number_of_buckets), edgecolor='black')
    plt.title('Histogram of Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Number of Movies')
    plt.show()

if __name__ == "__main__":
    movies = load_movie_data('/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv')
    rating_data = movies['Rating']
    bucket_size, number_of_buckets = determine_bucket_size(rating_data)
    plot_histogram(rating_data, bucket_size, number_of_buckets)