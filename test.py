import pandas as pd
import numpy as np

# Load the datasets
movies = pd.read_csv('ml-latest-small/movies.csv')
ratings = pd.read_csv('ml-latest-small/ratings.csv')

# Explore the data structure
print("Movies shape:", movies.shape)
print("Ratings shape:", ratings.shape)
print("\nFirst few movies:")
print(movies.head())