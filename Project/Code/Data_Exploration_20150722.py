# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
matching ethnicity based on ID
"""

import pandas as pd
import numpy as np

cross = pd.read_table('00_CrossSectional.tsv', low_memory=False)
cross.head()

baseline = pd.read_table('00_Baseline.tsv', low_memory=False)
baseline.head()

race_key = cross[['ID', 'ETHNIC']]

baseline_bp = baseline[['SWANID', 'SYSBP10', 'SYSBP20', 'SYSBP30']]

#drinks.rename(columns={'beer_servings':'beer', 'wine_servings':'wine'}, inplace=True)

cross.rename(columns{'ID':'SWANID'})

race_dict = dict(zip(race_key.ID, race_key.ETHNIC))

baseline_bp['ETHNIC'] = baseline_bp.SWANID.map(race_dict)

baseline_id = baseline[['SWANID']]
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


import numpy as np

baseline_bp.replace(' ',np.nan,inplace=True)

baseline_bp.isnull().sum()
baseline_bp.isnull().sum(axis=1)

 
BP_check = baseline_bp[baseline_bp.NumBP > 0]
BP_check.shape