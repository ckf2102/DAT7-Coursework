# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:50:27 2015

@author: Corinne
"""

import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data'
col_names = ['ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
glass = pd.read_csv(url, header=None, names=col_names)

# iris['species_num'] = iris.species.map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})

glass['binary'] = glass.Type.map({1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1})

feature_cols = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
X = glass[feature_cols]

y = glass.binary

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print metrics.accuracy_score(y_test, y_pred)

k_range = range(1, 51)
testing_error = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    # testing error
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    testing_error.append(1 - metrics.accuracy_score(y_test, y_pred))

%matplotlib inline

import matplotlib.pyplot as plt
plt.style.use('ggplot')

# plot the relationship between K and TESTING ERROR
plt.plot(k_range, testing_error)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Error')

count_0 = 0
count_1 = 0

for x in len(y_train):
    if x == 0:
        count_0 = count_0 + 1
    else:
        count_1 = count_1 + 1
