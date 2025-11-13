import pandas as pd     
import matplotlib.pyplot as plt 
import numpy as np

netflix_df = pd.read_csv("netflix_data.csv")
# Filter the data
movies = netflix_df[netflix_df["type"] == "Movie"] 
movies_1990s = movies[np.logical_and(movies["release_year"] >= 1990, movies["release_year"] <= 1999)]
# Vizualize distribution
plt.hist(movies_1990s["duration"])
plt.show() # 120 min most frequent 47 times
