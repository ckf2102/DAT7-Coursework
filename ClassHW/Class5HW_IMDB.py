'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''

# read in 'imdb_1000.csv' and store it in a DataFrame named movies

import pandas as pd
movies = pd.read_csv('imdb_1000.csv')

# check the number of rows and columns

movies.shape

# check the data type of each column

movies.dtypes

# calculate the average movie duration

movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies

movies.sort('duration')

# create a histogram of duration, choosing an "appropriate" number of bins

movies.duration.plot(kind='hist', bins=50)

# use a box plot to display that same data

movies.duration.plot(kind='box')

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings

movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels

import matplotlib.pyplot as plt

movies.content_rating.value_counts().plot(kind='bar', title = 'Ratings Frequency')
plt.xlabel('Content Ratings')
plt.ylabel('Frequency (# of movies)')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP

# ufo_col = [col.replace(' ','_') for col in ufo.columns]

unrated_dict = {'NOT RATED':'UNRATED', 'APPROVED':'UNRATED', 'PASSED':'UNRATED', 'GP':'UNRATED'}

movies['content_rating'].replace(unrated_dict, inplace = True)

# convert the following content ratings to "NC-17": X, TV-MA

nc_dict = {'X':'NC-17', 'TV-MA':'NC-17'}
movies['content_rating'].replace(nc_dict, inplace = True)

# count the number of missing values in each column

movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values

movies[movies.content_rating.isnull()]

movies.update(movies[movies.title == 'True Grit'].fillna("PG-13"))
movies.content_rating.fillna("PG", inplace = True)

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours

movies[movies.duration >= 120].star_rating.mean()
movies[movies.duration < 120].star_rating.mean()

# use a visualization to detect whether there is a relationship between star rating and duration

movies.plot(kind = "scatter", x = "duration", y = "star_rating", alpha = 0.3)

# calculate the average duration for each genre

movies.groupby('genre').duration.mean()


'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration

movies.groupby('content_rating').mean().drop("duration", axis = 1).plot(kind = "bar")

movies.boxplot(column = "star_rating", by = "content_rating")

# determine the top rated movie (by star rating) for each genre

movies.groupby('genre')['title'].star_rating.agg(['max'])


# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates

# calculate the average star rating for each genre, but only include genres with at least 10 movies

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
