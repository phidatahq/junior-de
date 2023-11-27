import pandas as pd

def most_common_director(file_path):
    df = pd.read_csv(file_path)
    return df['Director'].mode()[0]

if __name__ == "__main__":
    result = most_common_director('/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv')
    print(result)