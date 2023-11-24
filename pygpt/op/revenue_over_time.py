import csv
import os
from collections import defaultdict


def read_movie_data(file_path):
    # Read the CSV file and return the necessary data
    data = defaultdict(float)
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                year = int(row['Year'])
                revenue = float(row['Revenue (Millions)'])
                data[year] += revenue
            except ValueError:
                # Skip rows with missing/invalid data
                continue
    return data


def calculate_annual_revenue(movie_data):
    # Sort and return the data
    return dict(sorted(movie_data.items()))


if __name__ == "__main__":
    file_path = '/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv'
    movie_data = read_movie_data(file_path)
    annual_revenue = calculate_annual_revenue(movie_data)
    print(annual_revenue)