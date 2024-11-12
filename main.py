import pandas as pd
import matplotlib.pyplot as plt

# Reading dataset
def read_dataset(file_path):
    df = pd.read_csv(file_path)
    return df

# Data Exploring
def explore_data(df):
    print("Dataset Description:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("\nColumns:")
    print(df.columns)
    print("\nSample Data:")
    print(df.head())

# Cleaning data
def clean_data(df):
    # Displaing sum of missing values for each column
    print("\nMissing Values in Each Column:\n")
    print(df.isnull().sum())
    
    # Droping rows with missing values
    df.dropna(inplace=True)
    print("\nData cleaned successfully by dropping rows with missing values.")
    return df

# Data Analysis
def calculate_average(df, column):
    return df[column].mean()

def find_min_max(df, column):
    return df[column].min(), df[column].max()

def count_occurrences(df, column, value):
    return df[column].value_counts().get(value, 0)

def group_and_summarize(df, group_by_column, summarize_column):
    return df.groupby(group_by_column)[summarize_column].describe()

def plot_histogram(df, column):
    plt.hist(df[column], bins=10)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column}')
    plt.show()

# Command Line Interface CLI showing options and based on choice running specific function
def main():
    file_path = 'TB_outcomes_age_sex_2024-06-01.csv'
    df = read_dataset(file_path)
    
    while True:
        print("\nOptions:")
        print("1. Explore Data")
        print("2. Clean Data")
        print("3. Calculate Average")
        print("4. Find Min and Max")
        print("5. Count Occurrences")
        print("6. Group and Summarize")
        print("7. Plot Histogram")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            explore_data(df)
        elif choice == '2':
            df = clean_data(df)
            print("Data cleaned successfully.")
        elif choice == '3':
            column = input("Enter the column name to calculate average: ")
            if column in df.columns:
                print(f"Average of {column}: {calculate_average(df, column)}")
            else:
                print("Column not found.")
        elif choice == '4':
            column = input("Enter the column name to find min and max: ")
            if column in df.columns:
                min_val, max_val = find_min_max(df, column)
                print(f"Min of {column}: {min_val}")
                print(f"Max of {column}: {max_val}")
            else:
                print("Column not found.")
        elif choice == '5':
            column = input("Enter the column name: ")
            value = input("Enter the value to count occurrences: ")
            if column in df.columns:
                print(f"Occurrences of {value} in {column}: {count_occurrences(df, column, value)}")
            else:
                print("Column not found.")
        elif choice == '6':
            group_by_column = input("Enter the column name to group by: ")
            summarize_column = input("Enter the column name to summarize: ")
            if group_by_column in df.columns and summarize_column in df.columns:
                print(group_and_summarize(df, group_by_column, summarize_column))
            else:
                print("Column not found.")
        elif choice == '7':
            column = input("Enter the column name to plot histogram: ")
            if column in df.columns:
                plot_histogram(df, column)
            else:
                print("Column not found.")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
