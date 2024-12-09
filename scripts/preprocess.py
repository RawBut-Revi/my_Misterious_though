import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load the data from the given CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """
    Clean the data by handling missing values, converting types, etc.
    """
    # Drop rows with any missing values
    data.dropna(inplace=True)

    # Convert 'number' column to integer if it's not already
    data['number'] = data['number'].astype(int)
    
    return data

def preprocess_data(data):
    """
    Additional preprocessing steps like feature engineering.
    """
    # Example feature engineering: Calculate rolling mean of hot numbers
    data['rolling_mean'] = data['number'].rolling(window=5).mean().fillna(0)
    
    return data

def save_data(data, output_path):
    """
    Save the preprocessed data to a CSV file.
    """
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    # File paths
    input_file = '../data/roulette_data.csv'
    output_file = 'data/preprocessed_roulette_data.csv'

    # Load data
    data = load_data(input_file)

    # Clean data
    data = clean_data(data)

    # Preprocess data
    data = preprocess_data(data)

    # Save preprocessed data
    save_data(data, output_file)

    print("Data preprocessing complete. Preprocessed data saved to:", output_file)
