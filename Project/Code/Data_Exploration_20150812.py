#############################################################
#                                                           #
#                   What's in the data                      #
#                                                           #
#############################################################

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv', low_memory=False)

str_dis0_cols = ['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0']
str_dis1_cols = ['Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1']

demographics0_cols = ['DEGREE', 'MARITALGP', 'AGE0', 'STATUS0']
demographics1_cols = ['DEGREE', 'MARITALGP', 'AGE1', 'STATUS1']

latent_cols0 = ['disc0', 'pstress0', 'hostility']
latent_cols1 = ['disc1', 'pstress1', 'hostility']

baseline_cols = ['SWANID', 'Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility', 'AL0']
visit01_cols = ['SWANID', 'Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME1', 'DEGREE', 'MARITAL1', 'AGE1', 'STATUS1', 'disc1', 'pstress01', 'hostility', 'AL1']
change_data_cols = ['SWANID', 'Race_AfAm', 'Race_Hispanic', 'Race_White', 'INCOME0', 'DEGREE', 'MARITALGP', 'AGE0', 'STATUS0', 'disc0', 'pstress0', 'hostility', 'change']

baseline_data = data[baseline_cols]
visit01_data = data[visit01_cols]
change_data = data[change_data_cols]

data[['Race_AfAm', 'Race_Hispanic', 'Race_White', 'AL0']].corr()

sns.heatmap(baseline_data.corr())
sns.heatmap(visit01_data.corr())
sns.heatmap(change_data.corr())

baseline_corr = baseline_data.corr()
visit01_corr = visit01_data.corr()
change_data_corr = change_data.corr()

data.boxplot(column='AL0', by='ETHNIC')
data.boxplot(column='AL0', by='INCOME0')

data.boxplot(column='AL1', by = 'ETHNIC')
data.boxplot(column='AL1', by = 'INCOME1')

data.boxplot(column='change', by = 'ETHNIC')
data.boxplot(column='change', by = 'INCOME0')

data.plot(kind='scatter', x = 'disc0', y = 'AL0', alpha = 0.3)
data.plot(kind='scatter', x = 'pstress0', y = 'AL0', alpha = 0.3)
data.plot(kind='scatter', x = 'hostiliy', y = 'AL0', alpha = 0.3)

data.plot(kind = 'scatter', x = 'hostility', y = 'disc0')

data.change.plot(kind='hist', bins=12)
plt.xlabel('Change in AL score')
plt.ylabel('Frequency')