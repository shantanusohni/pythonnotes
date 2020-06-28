import pandas as pd
import matplotlib.pyplot as plt

rating = pd.read_csv('ml-1m/ratings.dat', sep='::',
                     names=['userId', 'movieId', 'rating'], engine='python',
                     usecols=[0,1,2])

movies = pd.read_csv('ml-1m/movies.dat', sep='::',
                     names=['movieId', 'moviename', 'genre'], engine='python',
                     usecols=[0,1,2])

movies_rating = pd.merge(movies, rating, on='movieId')
movies_rating.groupby('moviename').size().sort_values(ascending=False).head(5).plot(kind='barh')
plt.show()

# Plotting a graph in Python
fig, ax = plt.subplots()
movienames = list(df1.index)
y_pos = range(1, len(movienames) + 1)
x_pos = list(df1.values)

ax.barh(y_pos, x_pos, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(movienames)
ax.set_xlabel('Rating Count')
ax.set_title('Top 5 movies rating count')
plt.show()
