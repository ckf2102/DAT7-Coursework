# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:07:09 2015

@author: Corinne
"""

"""
Exercise: Human learning with iris data

Question: Can you predict the species of an iris using peteal and sepal measurements?

"""

"""
Task 1: Read the iris data into a pandas DataFrame, including colum names
"""

import pandas as pd

iris_cols = ['s_length', 's_width', 'p_length', 'p_width', 'iclass']
iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', names = iris_cols)


"""
Task 2: Gather some basic information about the data
"""

iris.describe()
iris.iclass.value_counts()

iris.isnull().sum()

"""
Task 3: Use groupby, sorting, and plotting to look for differences between species
"""

iris.groupby('iclass').describe()

iris.groupby('iclass').s_width.agg(['count', 'mean', 'min', 'max']).sort('mean')
iris.groupby('iclass').p_width.agg(['count', 'mean', 'min', 'max']).sort('mean')
iris.groupby('iclass').p_length.agg(['count', 'mean', 'min', 'max']).sort('mean')
iris.groupby('iclass').p_width.agg(['count', 'mean', 'min', 'max']).sort('mean')

iris.boxplot(column = 's_length', by = 'iclass')

iris.boxplot(column = 's_width', by = 'iclass')

iris.boxplot(column = 'p_length', by = 'iclass')

iris.boxplot(column = 'p_width', by = 'iclass')

iris.groupby('iclass').plot(kind='box')

iris.p_width.hist(by=iris.iclass, sharex = True, sharey = True, layout = (3,1))
iris.p_length.hist(by=iris.iclass, sharex = True, sharey = True, layout = (3,1))

iris['iclassnum'] = iris.iclass.map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
iris.plot(kind = 'scatter', x = 'p_width', y = 'p_length', c = 'iclassnum', colormap = 'Blues')

"""
Task 4: Write down a set of rules that coule be used to predict species based on measurements
"""

# Rule 1: if sepal width > petal length --> setosa
# Rule 2: if petal width < 1 --> setosa

print iris.iclass

"""
Bonus: Define function that accepts a row of data and returns a predicted species
Then use that function to make predictions for all existing rows of data
"""
    