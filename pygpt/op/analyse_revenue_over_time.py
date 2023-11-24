import pandas as pd

# Define a function to read the data from the movies file and extract the year and revenue.
def read_and_aggregate_revenue(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Check if 'Year' and 'Revenue_Millions' columns exist
    if 'Year' not in data.columns or 'Revenue_Millions' not in data.columns:
        return 'Missing required data columns. Please provide a file with Year and Revenue_Millions columns.'

    # Group the data by year and sum the revenue for each year
    revenue_by_year = data.groupby('Year')['Revenue_Millions'].sum().reset_index()

    # Sort the grouped data by year
    sorted_revenue = revenue_by_year.sort_values('Year')
    return sorted_revenue

# If this file is the main module, execute the following
if __name__ == '__main__':
    # Path to the movies CSV file
    movies_file_path = '/Users/zu/lab/templates/junior-de/data/imdb/Movies.csv'
    
    # Run the function and get the result
    revenue_over_time = read_and_aggregate_revenue(movies_file_path)
    print(revenue_over_time)