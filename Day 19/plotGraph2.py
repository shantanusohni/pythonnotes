import pandas as pd
import matplotlib.pyplot as plt

rating = pd.read_csv('ml-1m/ratings.dat', sep='::',
                     names=['userId', 'movieId', 'rating'], engine='python',
                     usecols=[0,1,2])

movies = pd.read_csv('ml-1m/movies.dat', sep='::',
                     names=['movieId', 'moviename', 'genre'], engine='python',
                     usecols=[0,1,2])

movies_rating = pd.merge(movies, rating, on='movieId')

users = pd.read_csv('ml-1m/users.dat', sep='::',
                     names=['userId', 'gender', 'age-group', 'profession'],
                     engine='python',
                     usecols=[0,1,2,3])
users_movies_rating = pd.merge(movies_rating, users, on='userId')

all_professions = {0:  "other or not specified",
                   1:  "academic/educator",
                      2:  "artist" ,3:  "clerical/admin" ,4:  "college/grad student" ,5:  "customer service",6:  "doctor/health care",7:  "executive/managerial" ,8:  "farmer" ,9:  "homemaker" ,10:  "K-12 student"
	,11:  "lawyer",12:  "programmer" ,13:  "retired" ,14:  "sales/marketing" ,15:  "scientist" ,16:  "self-employed"
	,17:  "technician/engineer",18:  "tradesman/craftsman" ,19:  "unemployed" ,20:  "writer"}

users_movies_rating = users_movies_rating.replace({"profession": all_professions})
users_movies_rating.groupby('profession').size().sort_values(ascending=False)[:5].plot.pie(y='profession', subplots=True, figsize=(6, 3))
plt.show()