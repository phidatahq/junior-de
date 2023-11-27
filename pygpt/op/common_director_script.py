import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path)

def most_common_director(data):
    return data['Director'].value_counts().idxmax()

if __name__ == "__main__":
    data = read_data('/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv')
    common_director = most_common_director(data)
    print(common_director)