#############################################################
#                                                           #
#          Putting together a linear regression             #
#                                                           #
#############################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn import metrics

data = pd.read_csv('data.csv', low_memory=False)

str_dis0_cols = ['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0']
str_dis1_cols = ['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1']

demographics0_cols = ['DEGREE', 'MARITALGP', 'AGE0', 'STATUS0']
demographics1_cols = ['DEGREE', 'MARITALGP', 'AGE1', 'STATUS1']

latent_cols0 = ['disc0', 'pstress0', 'hostility']
latent_cols1 = ['disc1', 'pstress01', 'hostility']

baseline_feature_combos = [
str_dis0_cols,
demographics0_cols,
latent_cols0,
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'disc0', 'pstress0', 'hostility'],
['DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility'],
['DEGREE', 'MARITALGP', 'AGE0'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'disc0', 'pstress0', 'hostility'],
['DEGREE', 'MARITALGP', 'AGE0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'INCOME0', 'DEGREE', 'hostility'],
['Race_AfAm', 'INCOME0', 'hostility']
]

baseline_feature_combos2 = [
['Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm','Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic','INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White','DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0','MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'STATUS0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'disc0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'pstress0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0']
]

visit01_feature_combos = [
str_dis1_cols,
demographics1_cols,
latent_cols1,
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'STATUS1'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'disc1', 'pstress01', 'hostility'],
['DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'pstress01', 'hostility'],
['DEGREE', 'MARITAL1', 'AGE1'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'disc1', 'pstress01', 'hostility'],
['DEGREE', 'MARITAL1', 'AGE1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'INCOME1', 'DEGREE', 'hostility'],
['Race_AfAm', 'INCOME1', 'hostility']
]

visit01_feature_combos2 = [
['Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm','Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic','INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White','DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1','MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'AGE1', 'STATUS1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'STATUS1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'disc1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'pstress01', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'hostility'],
['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'pstress01']
]

linreg=LinearRegression()

data['null_AL0'] = data.AL0.mean()
data['null_AL1'] = data.AL1.mean()
data['null_change'] = data.change.mean()

"""
null accuracy RSME
"""

# baseline AL
np.sqrt(metrics.mean_squared_error(data.null_AL0, data.AL0))
# 2.328 is the number to beat

# visit 1 AL
np.sqrt(metrics.mean_squared_error(data.null_AL1, data.AL1))
# 2.335 is the number to beat

"""
using cross-validation
"""

def lin_reg(data, feature_cols, outcome):
    X = data[feature_cols]
    y = data[outcome]
    return np.sqrt(-cross_val_score(linreg, X, y, cv=10, scoring='mean_squared_error')).mean()

RSME_baseline_cross_val = []

for x in baseline_feature_combos2:
    RSME_baseline_cross_val.append([x, lin_reg(data, x, 'AL0')])


RSME_visit01_cross_val = []

for x in visit01_feature_combos2:
    RSME_visit01_cross_val.append([x, lin_reg(data, x, 'AL1')])


for x in RSME_visit01_cross_val:
    print x[1]
 
"""
how well does the baseline-trained model do on visit 1 data?
"""

RMSE_testing_cross_val = []

for x in range(0, len(baseline_feature_combos)):
    X_train = data[baseline_feature_combos[x]]
    y_train = data.AL0
    X_test = data[visit01_feature_combos[x]]
    y_test = data.AL1
    linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    RMSE_testing_cross_val.append(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

#############################################################
#                                                           #
#                       Decision Trees                      #
#                                                           #
#############################################################

from sklearn.tree import DecisionTreeRegressor
treereg = DecisionTreeRegressor(max_depth=5, random_state=1)

def dec_tree(data, feature_cols, outcome):
    X = data[feature_cols]
    y = data[outcome]
    return np.sqrt(-cross_val_score(treereg, X, y, cv=10, scoring='mean_squared_error')).mean()

"""
checking max depth
"""

# list of values to try
max_depth_range = range(1, 20)

# going to look at max_depth over 4 different feature combos
RMSE_scores = []
for depth in max_depth_range:
    treereg = DecisionTreeRegressor(max_depth=depth, random_state=1)
    RMSE_scores.append(dec_tree(data, baseline_feature_combos[0], 'AL1'))
# plot max_depth (x-axis) versus RMSE (y-axis)
plt.plot(max_depth_range, RMSE_scores)
plt.xlabel('max_depth')
plt.ylabel('RMSE (lower is better)')

RMSE_scores = []
for depth in max_depth_range:
    treereg = DecisionTreeRegressor(max_depth=depth, random_state=1)
    RMSE_scores.append(dec_tree(data, baseline_feature_combos[1], 'AL0'))
# plot max_depth (x-axis) versus RMSE (y-axis)
plt.plot(max_depth_range, RMSE_scores)
plt.xlabel('max_depth')
plt.ylabel('RMSE (lower is better)')

RMSE_scores = []
for depth in max_depth_range:
    treereg = DecisionTreeRegressor(max_depth=depth, random_state=1)
    RMSE_scores.append(dec_tree(data, baseline_feature_combos[2], 'AL0'))
# plot max_depth (x-axis) versus RMSE (y-axis)
plt.plot(max_depth_range, RMSE_scores)
plt.xlabel('max_depth')
plt.ylabel('RMSE (lower is better)')

RMSE_scores = []
for depth in max_depth_range:
    treereg = DecisionTreeRegressor(max_depth=depth, random_state=1)
    RMSE_scores.append(dec_tree(data, baseline_feature_combos[3], 'AL0'))
# plot max_depth (x-axis) versus RMSE (y-axis)
plt.plot(max_depth_range, RMSE_scores)
plt.xlabel('max_depth')
plt.ylabel('RMSE (lower is better)')

"""
stick with max-depth = 5
"""

treereg = DecisionTreeRegressor(max_depth=5, random_state=1)

RSME_dec_tree = []

for x in visit01_feature_combos2:
    RSME_dec_tree.append(dec_tree(data, x, 'AL0'))

for x in RSME_dec_tree:
    print x

RMSE_testing_dec_tree = []

for x in range(0, len(baseline_feature_combos2)):
    X_train = data[baseline_feature_combos2[x]]
    y_train = data.AL0
    X_test = data[visit01_feature_combos2[x]]
    y_test = data.AL1
    treereg.fit(X_train, y_train)
    y_pred = treereg.predict(X_test)
    RMSE_testing_dec_tree.append(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

for x in RMSE_testing_dec_tree:
    print x
   

treereg.fit(data[visit01_feature_combos2[7]], data.AL1)
pd.DataFrame({'feature':visit01_feature_combos2[7], 'importance':treereg.feature_importances_}).sort('importance', ascending=False)
