import pandas as pd

def load_movie_data(file_path):
    """Loads the movie data from a CSV file."""
    return pd.read_csv(file_path)

def find_most_common_director(data):
    """Finds the most common director in the dataset."""
    return data['Director'].mode()[0]

if __name__ == "__main__":
    # Path to the movies CSV file
    movies_file_path = '/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv'
    # Load the movie data
    movies_data = load_movie_data(movies_file_path)
    # Find the most common director
    most_common_director = find_most_common_director(movies_data)
    print(f'The most common director is: {most_common_director}')