# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:21:14 2015

@author: Corinne
"""

"""
API

- Application Programming Interface
- Structured way to expose specific functionality and data access to users
    - i.e. being able to pull tag results from Twitter
    - Twitter offers API, and allows a way for authorized users to programmatically
        ask for data and get it back in a structured way
    - Using API key, programmatically ask Twitter for xyz
    - As the programmer, you have a specific way to get your data
    - Twitter has laid out how you can access data, how much you can get, etc
    - Also used to access functionality
    - API calls for functions (i.e. one that creates user, or some other action)
- Web APIs usually follow the "REST" standard

How to interact with a REST API
- Make a "request" to a specific URL (endpoint) and get data back in "response"
- Most relevant request method for us is GET (other methods: POST, PUT, DELETE)
- Response is often JSON format
- Web console is sometimes available (allows you to explore an API)
"""

import pandas as pd
movies = pd.read_csv('imdb_1000.csv')
movies.head()

# wouldn't it be nice if there was a year column?
# find a way to get year from API (supplementing data)

# API call is an endpoint followed by parameters
# OMDb: web console to test theories, as well as table to tell you what
# you need in your query

# URLs tend to be
# http://domain.com/?parameter&parameter2&parameter3

# use requests library to interact with a URL

import requests
r = requests.get('http://www.omdbapi.com/?t=the+shawshank+redemption&r=json&type=movie')

# call is simplified, and add type (movie)
# could also remove the spaces
# http://www.omdbapi.com/?t=the+shawshank+redemption&y=&plot=short&r=json
# URL does not specify what the response is going to be, but it is the request (filters)
# they have already defined the response rules

# check the status: 200 means success, 4xx means error
r.status_code

#view the raw response text (attribute)
r.text
    # it looks like a dictionary, but it is in fact... a super long string
    # but it looks like what we want so we're still good

# decode the JSON response body into a dictionary (method)
r.json()
    # now we get back a dictionary

# extracting year from the dictionary
r.json()['Year']

d = r.json()
d['Year']

# what happens if the movie name is not recognized?
trash = requests.get('http://www.omdbapi.com/?t=a;lskdjf&r=json&type=movie')
trash.status_code
    # it gives us a success
    # API defines what's success or failure
trash.text
    # {"Response":"False","Error":"Movie not found!"}
    # note there is a "Response" in r.text
    # now we know that we can do an if statement (if Response = True, find the year
    # otherwise movie title not in )

# define a function to return the year
def get_movie_year(title):
    r = requests.get('http://www.omdbapi.com/?t=' + title + '&r=json&type=movie')
        # building a URL out of a parameter
    info = r.json()
    if info['Response'] == 'True':
        return int(info['Year'])
    else:
        return 0
            # this way you have an elegant way of finding missing values in a dataframe
get_movie_year('The Shawshank Redemption')

get_movie_year('blahblah')
    # throws error
    # since info's dictionary doesn't have Year


# now we need to write the for loop that will print the years

# let's test out on a smaller dataframe
topmovies = movies.head().copy()
    # without the .copy(), you're making a pointer to the original
    # instead of a copy.

# now we write the for loop
from time import sleep
    # most APIs have rate limit
    # make the assumption 

years = []
for title in topmovies.title:   # can iterate through series like a list
    years.append(get_movie_year(title))
    sleep(1)
        # limit to one call per second
        # this is considered pretty slow

# assertions
assert(len(topmovies) == len(years))
    # if the length is different, that means that something failed
    # you want Python script to raise an error
    # useful tool to check assumptions

# save list as a new column (length must be the same)
topmovies['year'] = years

'''
Bonus content: Updating the DataFrame as part of a loop
'''

# enumerate allows you to access the item location while iterating
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print index, letter

# iterrows method for DataFrames is similar
for index, row in topmovies.iterrows():
    print index, row['title']

# create a new column and set a default value
movies['year'] = -1

# loc method allows you to access a DataFrame element by 'label'
movies.loc[0, 'year'] = 1994

# write a for loop to update the year for the first three movies
for index, row in movies.iterrows():
    if index < 3:
        movies.loc[index, 'year'] = get_movie_year(row['title'])
        sleep(1)
    else:
        break

'''
Other considerations when accessing APIs:
- Most APIs require you to have an access key
- Most APIs limit the number of API calls you can make (per day, hour, minute, etc.)
- Not all APIs are free
- Not all APIs are well-documented
- Pay attention to the API version

Python wrapper is another option for accessing an API:
- Set of functions that "wrap" the API code for ease of use
- Potentially simplifies your code
- But, wrapper could have bugs or be out-of-date or poorly documented
'''



