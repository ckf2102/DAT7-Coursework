# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:24:26 2015

@author: Corinne
"""

# Pandas! Cute
# check the posted code file later for extra

import pandas as pd
    # pd just makes it easier to reference the pandas

pd.read_table('u.user')
    # thinks the first line of data is the header... nope.
    # also thinks it's one column...

# can read from a URL
# pd.read_table('url')

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
    # makes reading in the names of the columns easier

users = pd.read_table('u.user', sep='|', header=None, names=user_cols, index_col='user_id', dtype={'zip_code':str})
    # sep: indicates the separator is '|'
    # None is a special object, like True and False
    # index_col: can replace with what you want or just use the default
        # in a sense, we've lost the col user_id as a column, now an index
        # for some reason, index does not have to be unique...??

'''
Getting a sense of the data
'''

users                   # will show first and last 30 records
type(users)             # shows the type
users.head(10)          # OO, default is 5
users.tail(10)          # same as .head()
    # method
users.index             # shows the index, aka labels
    # attribute
users.columns           # will see the column names

users.dtypes            # will show the types for each column
                            # object will typically refer to string
                            # datatypes from numpy
users.shape             # shows a tuple, (r, c)
users.values            # looking at the numpy array

# numpy is a speed optimized python library that panda is built on

users['gender']         # selects one column using column name, returns a series
users.gender            # bc typing the brackets and quotation is tough
                            # when you name columns panda automatically makes them attributes

users.describe()        # describes all numeric columns (mean, std, etc)
users.describe(include=['object'])
                        # qualitative descriptions for objects (count, freq, mode/top)
users.describe(include='all')

users.head()                # dataframe method
users.gender.describe()     # series method
users.age.mean()

users.gender.value_counts()     # count of occurrences for each value
users.age.value_counts()

'''
Exercise 1
'''

drinks = pd.read_table('drinks.csv', sep=',')
    # there's also a pd.read_csv('csv file name') but read_table is all inclusive

# broadcasting an operation throughout a series
drinks.beer_servings * 10
    # will multiply everything by 10

# calculate avg beer_savings for entire dataset
drinks.beer_servings.mean()

# count num of occurrences of each 'continent' and see if it looks correct
drinks.continent.value_counts()
    # missing north america bc for some reason the string 'NA' is read in as NA()


'''
Filtering
'''

# logical filtering: only show users with certain attribute
users.age < 20          # will return a series with type bool... creates the logical series
users[users.age<20]     # creates a series of only records with age < 20

# create a boolean series to do something with later
young_bool = users.age < 20     # create a series of bools
users[young_bool]               # and use the series to filter the rows
users[users.age < 20]           # same as above, combines the steps
    # need to make sure that size is identical
    # think of bracket of generalized operator for filtering out stuff
    # you've now created another series

# data frame = rows and columns
# series = just one column! will only return # of rows

# pulling out occupation of users younger than 20
users[users.age < 20].occupation.value_counts()
    # users = data frame
    # [users.age < 20] = data frame
    # .occupation = series

# filtering multiple conditions
users[(users.age < 20) & (users.gender == "M")]
    # need to wrap in paranthesis because & evaluated first
    # users that are under 20 and male
users[(users.age < 20) | (users.age > 60)]
    # under 20 or over 60

# if you're doing multiple OR conditions for the same column
users[users.occupation.isin(["doctor", "lawyer"])]

'''
Sorting
'''

# to sort series, use order() method
users.age.order()
    # returns series
    # that's great, but more likely it would be nice to keep the whole data frame

users.sort('age')
    # returns data frame
users.sort('age', ascending=False)  # reverse
users.sort(['occupation','age'])    # sort on multiple columns

'''
Exercise
'''

# filter to include only EU countries

drinks[drinks.continent == 'EU']

# filter DataFrame to include EU countries with wine > 300

drinks[(drinks.continent == 'EU') & (drinks.wine_servings > 300)]

# calc avg beer_servings for all of Europe

drinks[drinks.continent == 'EU'].beer_servings.mean()

# determine which 10 countries have the highest total litres of pure alcohol

drinks.sort('total_litres_of_pure_alcohol', ascending=False).country.head(10)

# showing multiple columns: pass list of columns as strings
# requires two brackets
drinks.sort('total_litres_of_pure_alcohol', ascending=False)[['country','total_litres_of_pure_alcohol']].head(10)

'''
Renaming
'''
# renaming one or more columns
drinks.rename(columns={'beer_servings':'beer', 'wine_servings':'wine'})
    # when printed, doesn't change the column names
    # changes temporarily
    # would have to do drinks = drinks.rename but that can be memeory inefficient
drinks.rename(columns={'beer_servings':'beer', 'wine_servings':'wine'}, inplace=True)
    # will keep the renames inplace

# just replace the column names from the beginning
drink_cols = ['country', 'beer', 'spirit', 'wine', 'liters', 'continent']
drinks = pd.read_csv('drinks.csv', header=0, names=drink_cols)  
    # have to say header = 0 so it knows to override 0th row
    # replace during file reading
    # why is this important?
        # CAN'T ACCESS SERIES IF COLUMN NAME HAS A SPACE derp

# to replace after it's been read
drinks.columns = drink_cols

'''
Skipped in class
'''

# add a new column as a function of existing columns
drinks['servings'] = drinks.beer + drinks.spirit + drinks.wine
drinks['mL'] = drinks.liters * 1000

# removing columns
drinks.drop('mL', axis=1)                               # axis=0 for rows, 1 for columns
drinks.drop(['mL', 'servings'], axis=1)                 # drop multiple columns
drinks.drop(['mL', 'servings'], axis=1, inplace=True)   # make it permanent

'''
Missing values
'''

drinks.continent.value_counts()
    # excludes the missing values from the counts
    # so nothing from north america (NA)
drinks.continent.value_counts(dropna=False)
    # includes missing values
    # NaN = Not a Number

# finding the missing values in a series
drinks.continent.isnull()
    # series of bool type
drinks[drinks.continent.isnull()]
    # data frame of north american countries
    # isnull vs notnull

drinks.continent.isnull().sum()
    # converts True = 1 and False = 0

drinks.isnull()
    # data frame of T/F
drinks.isnull().sum()
    # checking for null values!!!
    # this is very useful
    # sums down a column

# Axis 0 = going down (down a series)
# Axis 1 = going across (across the entire record)
drinks.isnull().sum(axis=1)

# dropping missing values
drinks.dropna()
    # drops a row if ANY values are missing
drinks.dropna(how='all')
    # drops a row only if ALL values are missing

# fill in the missing values
drinks.continent.fillna(value="NA", inplace = True)
    # fill in with 'NA'

'''
Exercise
(complete before Monday)
'''

# read ufo.csv into a DataFrame called 'ufo'
ufo = pd.read_table('ufo.csv', sep = ",")

ufo_cols = ["city", "colors", "u_shape", "state", "time"]
ufo.columns = ufo_cols

# check the shape of the DataFrame
ufo.shape

# what are the three most common colors reported?
ufo.colors.value_counts().head(3)

# rename any columns with spaces so that they don't contain spaces

# see above

# for reports in VA, what's the most common city?

ufo[ufo.state == "VA"].city.value_counts().head(1)

# print a DataFrame containing only reports from Arlington, VA

ufo[(ufo.state == "VA") & (ufo.city == "Arlington")]

# count the number of missing values in each column

ufo.city.isnull().sum()
ufo.colors.isnull().sum()
ufo.u_shape.isnull().sum()
ufo.state.isnull().sum()
ufo.time.isnull().sum()

# how many rows remain if you drop all rows with any missing values?

ufo = ufo.dropna()






