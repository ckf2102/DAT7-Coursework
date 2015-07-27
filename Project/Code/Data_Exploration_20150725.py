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

baseline_bp = baseline[['SWANID', 'SYSBP10', 'SYSBP20', 'SYSBP30']]

cross.rename(columns={'ID':'SWANID'}, inplace=True)

race_key = cross[['SWANID','ETHNIC']]

# race_dict = dict(zip(race_key.ID, race_key.ETHNIC))
# baseline_bp['ETHNIC'] = baseline_bp.SWANID.map(race_dict)
# baseline_id = baseline[['SWANID']]
# baseline_id['ETHNIC'] = baseline_id.SWANID.map(race_dict)

baseline_bp = pd.merge(baseline_bp, race_key)

baseline_bp.isnull().sum()
baseline_bp.isnull().sum(axis=1)

"""
getting shapes for data sets
"""

cross.shape
baseline.shape

visit01 = pd.read_table('01_Visit1.tsv', low_memory=False)
visit01.shape

visit02 = pd.read_table('02_Visit2.tsv', low_memory=False)
visit02.shape

visit03 = pd.read_table('03_Visit3.tsv', low_memory=False)
visit03.shape

visit04 = pd.read_table('04_Visit4.tsv', low_memory=False)
visit04.shape

visit05 = pd.read_table('05_Visit5.tsv', low_memory=False)
visit05.shape

"""
getting selected dtypes
"""

cross.dtypes

cross_select = cross[['ID', 'ETHNIC', 'DEGREE', 'MARITALGP']]
cross_select.dtypes

baseline_select = baseline[['COURTES0', 'RESPECT0', 'POORSER0', 'NOTSMAR0', 'AFRAIDO0', 'DISHONS0', 'BETTER0', 'INSULTE0', 'HARASSE0', 'IGNORED0']
baseline_select.dtypes

"""
Discrimination Check
"""

disc_cols0 = ['COURTES0', 'RESPECT0', 'POORSER0', 'NOTSMAR0', 'AFRAIDO0', 'DISHONS0', 'BETTER0', 'INSULTE0', 'HARASSE0', 'IGNORED0']
disc_cols1 = ['COURTES1', 'RESPECT1', 'POORSER1', 'NOTSMAR1', 'AFRAIDO1', 'DISHONS1', 'BETTER1', 'INSULTE1', 'HARASSE1', 'IGNORED1']
disc_cols2 = ['SWANID', 'COURTES2', 'RESPECT2', 'POORSER2', 'NOTSMAR2', 'AFRAIDO2', 'DISHONS2', 'BETTER2', 'INSULTE2', 'HARASSE2', 'IGNORED2']
disc_cols3 = ['SWANID', 'COURTES3', 'RESPECT3', 'POORSER3', 'NOTSMAR3', 'AFRAIDO3', 'DISHONS3', 'BETTER3', 'INSULTE3', 'HARASSE3', 'IGNORED3']

baseline_disc = baseline[disc_cols0]
# visit01_disc = visit01[disc_cols1]
visit02_disc = visit02[disc_cols2]
visit03_disc = visit03[disc_cols3]

visit01_disc['SWANID'] = visit01['SWANID']
visit01_disc[disc_cols1] = visit01[disc_cols1]

baseline_disc['SWANID'] = baseline['SWANID']
baseline_disc[disc_cols0] = baseline[disc_cols0]


baseline_disc.replace(' ',np.nan,inplace=True)
baseline_disc.replace('-9', np.nan,inplace=True)

#baseline_disc[['COURTES0', 'RESPECT0', 'POORSER0', 'NOTSMAR0', 'AFRAIDO0', 'DISHONS0', 'BETTER0', 'INSULTE0', 'HARASSE0', 'IGNORED0']] = baseline_disc[['COURTES0', 'RESPECT0', 'POORSER0', 'NOTSMAR0', 'AFRAIDO0', 'DISHONS0', 'BETTER0', 'INSULTE0', 'HARASSE0', 'IGNORED0']].astype(float)

#baseline_disc['disc'] = baseline_disc[['COURTES0', 'RESPECT0', 'POORSER0', 'NOTSMAR0', 'AFRAIDO0', 'DISHONS0', 'BETTER0', 'INSULTE0', 'HARASSE0', 'IGNORED0']].mean(axis=1)

baseline_disc[disc_cols0] = baseline_disc[disc_cols0].astype(float)
baseline_disc['disc'] = baseline_disc[disc_cols0].mean(axis=1)

baseline_disc.disc.describe()

"""
getting quartile for Systolic BP
"""

# replace " " with NaN so that converting to float won't throw an error
baseline_bp.replace(' ',np.nan,inplace=True)

# convert to float
baseline_bp[['SYSBP10', 'SYSBP20', 'SYSBP30']] = baseline_bp[['SYSBP10','SYSBP20','SYSBP30']].astype(float)

# find mean of SYSBP
baseline_bp['SYSBP_mean'] = baseline_bp[['SYSBP10', 'SYSBP20', 'SYSBP30']].mean(axis=1)

# finding 75% of SYSBP
SYSBP_75 = baseline_bp.SYSBP_mean.quantile(.75)
SYSBP_max = baseline_bp.SYSBP_mean.max()

# initializing SYSBP score column
baseline_bp['SYSBP_sc'] = 0

# anything within 75% to max of SYSBP given a score of 1
baseline_bp.loc[baseline_bp.SYSBP_mean.between(SYSBP_75, SYSBP_max), 'SYSBP_sc'] = 1

# run this, try to figure out loc thing
baseline_bp[baseline_bp.SYSBP_mean > SYSBP_75].SYSBP_sc = 1