import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to read the movies data
def read_movies_data(file_path):
    return pd.read_csv(file_path)

# Function to generate and save histogram
def generate_histogram(data, num_bins, file_name):
    plt.hist(data, bins=num_bins, edgecolor='black')
    plt.title('Histogram of Movies by Rating')
    plt.xlabel('Rating')
    plt.ylabel('Number of Movies')
    plt.savefig(file_name)
    plt.close()

if __name__ == "__main__":
    # Path to the movies CSV file
    file_path = '/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv'
    # Read the movies data
    movies_df = read_movies_data(file_path)
    # Determine the range of movie ratings
    min_rating = movies_df['Rating'].min()
    max_rating = movies_df['Rating'].max()
    # Decide the bucket size: aiming for a bucket every 0.5 points
    bucket_size = 0.5
    num_bins = int((max_rating - min_rating) / bucket_size)
    # Generate and save histogram
    histogram_file = 'movies_rating_histogram.png'
    generate_histogram(movies_df['Rating'], num_bins, histogram_file)