# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 20:40:14 2015

@author: Corinne
"""

"""
Read titanic.csv into a DataFrame.
Define Pclass and Parch as the features, and Survived as the response.
Split the data into training and testing sets.
Fit a logistic regression model and examine the coefficients to confirm that they make intuitive sense.
Make predictions on the testing set and calculate the accuracy.
Bonus: Compare your testing accuracy to the "null accuracy", a term we've seen once before.
Bonus: Add Age as a feature, and calculate the testing accuracy. There will be a small issue you'll have to deal with.
"""

import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT7/master/data/titanic.csv')

feature_cols = ['Pclass', 'Parch']
X = data[feature_cols]
y = data.Survived

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

