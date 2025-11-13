import pandas as pd     
import matplotlib.pyplot as plt 
import numpy as np

netflix_df = pd.read_csv("netflix_data.csv")
# Filter the data
movies = netflix_df[netflix_df["type"] == "Movie"] 
movies_1990s = movies[np.logical_and(movies["release_year"] >= 1990, movies["release_year"] <= 1999)]
# Vizualize distribution
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (min)')
plt.ylabel("Number of Movies")
plt.show() 
duration = 100 # 100-120 min most frequent 47 times
# Count the number of short action movies from the 1990s
action_movies_1990s = movies_1990s[movies["genre"] == "Action"]
short_movie_count = 0
for movie_duration in action_movies_1990s["duration"]:
    if movie_duration < 90:
        short_movie_count += 1
print(short_movie_count)
