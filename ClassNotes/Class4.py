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
















