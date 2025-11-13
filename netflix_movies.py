import pandas as pd     
import matplotlib.pyplot as plt 
import numpy as np

netflix_df = pd.read_csv("netflix_data.csv")
# Most frequent duration
movies = netflix_df[netflix_df["type"] == "Movie"] 
movies_1990s = movies[np.logical_and(movies["release_year"] >= 1990, movies["release_year"] <= 1999)]
print(movies_1990s)
# After 1990 and below 2000