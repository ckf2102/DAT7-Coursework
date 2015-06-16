# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:15:40 2015

@author: Corinne
"""

# Data Visualization!

import pandas as pd
import matplotlib.pyplot as plt

# pandas ultimately just calls matplotlib
    # makes it a little easier to use matplotlib

# read in the drinks data
drink_cols = ['country', 'beer', 'spirit', 'wine', 'liters', 'continent']
drinks = pd.read_csv('drinks.csv', header=0, names=drink_cols, na_filter=False)

# read in the ufo data
ufo = pd.read_csv('ufo.csv')
ufo['Time'] = pd.to_datetime(ufo.Time)
    # can take a date/time represented as string and convert to datetime type
    # once your col is a datetime type, you can do other cool functions
ufo['Year'] = ufo.Time.dt.year
    # extracts out the year from the datetime type

"""
Histograms
"""

# sort beer column and split it into 3 groups
drinks.beer.order().values
    # .values (attribute) will allow you to see all data

# want to divide into 3 groups, so we see that the max is 376
    # equal value- 0-125, 126-250, 251-376

drinks.beer.plot(kind='hist', bins=3)
    # default bins = 10
    # always for one numeric variable

drinks.beer.plot(kind='hist', bins=20, title='Histogram of Beer Servings')
    # unfortunately x and y are not in arguments
plt.xlabel('Beer Servings')
plt.ylabel('Frequeny')
    # need to run all three at once

# compare with density plot (smooth version of a histogram)
drinks.beer.plot(kind='density', xlim=(0,500))
    # weird bc the hump doesn't start at 0

# stacked histogram with multiple variables
drinks[['beer', 'spirit', 'wine']].plot(kind='hist', stacked=True)
    # select multiple columns with double bracks

"""
Scatterplots
"""

# show relationship between two numerical variables

# is there a relationship between beer and wine?

# without a scatterplot
drinks[['beer', 'wine']].sort('beer').values

# with a scatterplot
drinks.plot(kind='scatter', x = 'beer', y = 'wine')

# to avoid overplotting, add transparency to be able to see multiple points
# in same location better
drinks.plot(kind='scatter', x = 'beer', y = 'wine', alpha=0.3)

# how about also adding another dimension by color
drinks.plot(kind='scatter', x = 'beer', y = 'wine', c = 'spirit', colormap = 'Blues')
    # darker color is higher spirit servings
    # default colormap is Black

# scatter matrix of three numerical columns
pd.scatter_matrix(drinks[['beer', 'spirit', 'wine']])
    # scatter plots of each pair of things

# increase figure size
pd.scatter_matrix(drinks[['beer', 'spirit', 'wine']], figsize=(10, 8))
    # pass a tuple to make it bigger or change the shape

"""
Bar plot
Show numerical comparison across different categories
"""

# count the number of countries in each continent
drinks.continent.value_counts()

# compare with bar plot
drinks.continent.value_counts().plot(kind='bar')
    # x axis is categories
    # pandas orders by what value_counts give them

# calculate the average beer/spirit/wine amounts for each continent
drinks.groupby('continent').mean().drop('liters', axis=1)
    # drop method: name the column you want to drop, and then the axis

# multiple side-by-side bar plots
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar')

# stacked bar plots
drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar', stacked=True)

# Axis reminder
    # by default, Axis = 0 for drop which is the row axis
    # axis defines the movement of the function

"""
Box plots
Show quartiles (and outliers) for one or more numerical variables
"""

# show "five-number summary" for beer
drinks.beer.describe()

# compare with box plot
drinks.beer.plot(kind='box')

# include multiple variables
drinks.drop('liters', axis=1).plot(kind='box')
    # any outliers are represented by +

"""
Line plot
Show the trend of a numerical variable over time
Good for time series
"""

# count the number of ufo reports each year (and sort by year)
ufo.Year.value_counts().sort_index()

# compare with line plot
ufo.Year.value_counts().sort_index().plot()

# don't use a line plot when there is no logical ordering
drinks.continent.value_counts().plot()







