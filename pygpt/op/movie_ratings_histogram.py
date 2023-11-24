import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a function to read data from the CSV file
def read_movie_data(file_path):
    return pd.read_csv(file_path)

# Define a function to determine the best bucket size for the histogram
def find_best_bucket_size(data_series):
    # Using Freedman-Diaconis rule to find the optimal number of bins
    iqr = np.subtract(*np.percentile(data_series, [75, 25]))
    bin_width = 2 * iqr * (len(data_series) ** (-1/3))
    bins = int(np.ceil((data_series.max() - data_series.min()) / bin_width))
    return bins

# Define a function to plot the histogram
def plot_histogram(data, bins):
    plt.hist(data, bins=bins, edgecolor='black')
    plt.title('Histogram of Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Number of Movies')
    plt.show()

# If this script is the main program
if __name__ == "__main__":
    # Path to the movies CSV file
    file_path = '/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv'

    # Read the movie data
    movies = read_movie_data(file_path)

    # Calculate the best bucket size
    optimal_bins = find_best_bucket_size(movies['Rating'])

    # Plot the histogram with the best bucket size
    plot_histogram(movies['Rating'], optimal_bins)