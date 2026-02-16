import pandas as pd

def calculate_average_score(filename):
    # Read the file
    df = pd.read_csv(filename)
    # Calculate the mean
    average = df['score'].mean()
    return average