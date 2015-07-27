# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
matching ethnicity based on ID
"""

import pandas as pd

cross = pd.read_table('00_CrossSectional.tsv')
cross.head()

baseline = pd.read_table('00_Baseline.tsv')
baseline.head()

race_key = cross[['ID', 'ETHNIC']]

baseline_id = baseline[['SWANID']]

race_dict = dict(zip(race_key.ID, race_key.ETHNIC))

baseline_id['ETHNIC'] = baseline_id.SWANID.map(race_dict)

"""
getting shapes for data sets
"""

cross.shape
baseline.shape

visit01 = pd.read_table('01_Visit1.tsv')
visit01.shape

visit02 = pd.read_table('02_Visit2.tsv')
visit02.shape

visit03 = pd.read_table('03_Visit3.tsv')
visit03.shape

visit04 = pd.read_table('04_Visit4.tsv')
visit04.shape

visit05 = pd.read_table('05_Visit5.tsv')
visit05.shape

"""
getting quartile for Systolic BP
"""

#feature_cols = ['SWANID', 'SYSBP10', 'SYSBP20', 'SYSBP30']
import csv

with open('00_Baseline.tsv', 'rU') as f:
    baseline = [row for row in csv.reader(f, delimiter='\t')]
    
header = baseline[0]
baseline = baseline[1:]