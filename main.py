# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

netflix_df = pd.read_csv("netflix_data.csv", index_col=0)

#print(netflix_df)

netflix_subset = netflix_df[netflix_df['type']== "Movie" ]
print(netflix_subset)

netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

#print(netflix_movies)

short_movies = netflix_movies[netflix_movies["duration"] < 60]
#print(short_movies)

colors = []
for index, row in netflix_movies.iterrows():
    if "Children" in row["genre"]:
        colors.append("blue")
    elif "Documentaries" in row["genre"]:
        colors.append("green")
    elif "Stand-Up" in row["genre"]:
        colors.append("red")
    else:
        colors.append("gray")
        
#plt.scatter(netflix_movies.index, netflix_movies["netflix movies"])
fig = plt.figure(figsize=(10, 6))
plt.scatter(netflix_movies["release_year"], netflix_movies["duration"], c=colors)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")
plt.show()

answer = "no"
