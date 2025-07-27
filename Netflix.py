# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")


# filtering movies
movies_90s = netflix_df[
    (netflix_df['type'] == 'Movie') & 
    (netflix_df['release_year'] >= 1990) & 
    (netflix_df['release_year'] <= 1999)
]

duration = int(movies_90s['duration'].mode()[0])
print("Most frequent duration:", duration)

short_action = movies_90s[
    (movies_90s['genre'].str.contains("Action", na=False)) &
    (movies_90s['duration'] < 90)
]

short_movie_count = short_action.shape[0]
print("Short action movies count:", short_movie_count)

movies_90s['duration'].plot(kind='hist', bins=20, title="Movie Durations in the 90s")
plt.xlabel("Duration (minutes)")
plt.show()
