import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path)

def most_common_director(data):
    return data['Director'].mode()[0]

if __name__ == "__main__":
    file_path = '/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv'
    movies_data = read_csv(file_path)
    common_director = most_common_director(movies_data)
    print(common_director)