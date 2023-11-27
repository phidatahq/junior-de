import pandas as pd


def read_csv(file_path):
    return pd.read_csv(file_path)


def revenue_over_time(df):
    revenue_time_data = df.groupby('Year')['Revenue_Millions'].sum().reset_index()
    return revenue_time_data.to_dict('records')


if __name__ == "__main__":
    movies_df = read_csv('/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv')
    revenue_data = revenue_over_time(movies_df)
    print(revenue_data)