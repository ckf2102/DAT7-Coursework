
#############################################################
#                                                           #
#             Reading and Basic Cleaning                    #
#                                                           #
#############################################################

import pandas as pd
import numpy as np

cross = pd.read_table('00_CrossSectional.tsv', low_memory=False)
baseline = pd.read_table('00_Baseline.tsv', low_memory=False)

cross.rename(columns={'ID':'SWANID'}, inplace=True)

visit01 = pd.read_table('01_Visit1.tsv', low_memory=False)
visit02 = pd.read_table('02_Visit2.tsv', low_memory=False)
visit03 = pd.read_table('03_Visit3.tsv', low_memory=False)
visit04 = pd.read_table('04_Visit4.tsv', low_memory=False)
visit05 = pd.read_table('05_Visit5.tsv', low_memory=False)

#############################################################
#                                                           #
#                   Discrimination                          #
#                                                           #
#############################################################

disc_cols0 = ['SWANID', 'COURTES0', 'RESPECT0', 'POORSER0', 'NOTSMAR0', 'AFRAIDO0', 'DISHONS0', 'BETTER0', 'INSULTE0', 'HARASSE0', 'IGNORED0']
disc_cols1 = ['SWANID', 'COURTES1', 'RESPECT1', 'POORSER1', 'NOTSMAR1', 'AFRAIDO1', 'DISHONS1', 'BETTER1', 'INSULTE1', 'HARASSE1', 'IGNORED1']
disc_cols2 = ['SWANID', 'COURTES2', 'RESPECT2', 'POORSER2', 'NOTSMAR2', 'AFRAIDO2', 'DISHONS2', 'BETTER2', 'INSULTE2', 'HARASSE2', 'IGNORED2']
disc_cols3 = ['SWANID', 'COURTES3', 'RESPECT3', 'POORSER3', 'NOTSMAR3', 'AFRAIDO3', 'DISHONS3', 'BETTER3', 'INSULTE3', 'HARASSE3', 'IGNORED3']

baseline_disc = baseline[disc_cols0]
visit01_disc = visit01[disc_cols1]
visit02_disc = visit02[disc_cols2]
visit03_disc = visit03[disc_cols3]

"""
def create_df(origdata, col_names, newdata, newcol):
    newdata = origdata[col_names]
    newdata.replace(' ', np.nan,inplace = True)
    newdata.replace('-9', np.nan, inplace=True)
    newdata[col_names[1:]] = newdata[col_names[1:]].astype(float)
    newdata.loc[:, newcol] = newdata[col_names[1:]].mean(axis=1)
    newdata.drop(newdata[col_names[1:]], axis=1, inplace=True)
"""

# replacing null values 

baseline_disc.replace(' ',np.nan,inplace=True)
baseline_disc.replace('-9', np.nan,inplace=True)

visit01_disc.replace(' ',np.nan,inplace=True)
visit01_disc.replace('-9', np.nan,inplace=True)

visit02_disc.replace(' ',np.nan,inplace=True)
visit02_disc.replace('-9', np.nan,inplace=True)

visit03_disc.replace(' ',np.nan,inplace=True)
visit03_disc.replace('-9', np.nan,inplace=True)

# changing type to float and calculating discrimination average

baseline_disc[disc_cols0[1:]] = baseline_disc[disc_cols0[1:]].astype(float)
baseline_disc['disc0'] = baseline_disc[disc_cols0[1:]].mean(axis=1)

visit01_disc[disc_cols1[1:]] = visit01_disc[disc_cols1[1:]].astype(float)
visit01_disc['disc1'] = visit01_disc[disc_cols1[1:]].mean(axis=1)

visit02_disc[disc_cols2[1:]] = visit02_disc[disc_cols2[1:]].astype(float)
visit02_disc['disc2'] = visit02_disc[disc_cols2[1:]].mean(axis=1)

visit03_disc[disc_cols3[1:]] = visit03_disc[disc_cols3[1:]].astype(float)
visit03_disc['disc3'] = visit03_disc[disc_cols3[1:]].mean(axis=1)

# Merging on SWANID 
discrimination = pd.merge(baseline_disc, visit01_disc)
discrimination = pd.merge(discrimination, visit02_disc)
discrimination = pd.merge(discrimination, visit03_disc)

## NOTE:    although the shape of visit03_disc = (2710, 12), the 
##          shape of discrimination = (2478, 45). Not only is there
##          loss to follow-up, but participants who may have skipped
##          visit01 could be re-evaluated for visit03
##          I could use an outer join, to capture all participants, even
##          those lost to follow-up if I wanted to


# dropping extraneous columns 

discrimination.drop(discrimination[disc_cols0[1:]], axis=1, inplace = True)
discrimination.drop(discrimination[disc_cols1[1:]], axis=1, inplace = True)
discrimination.drop(discrimination[disc_cols2[1:]], axis=1, inplace = True)
discrimination.drop(discrimination[disc_cols3[1:]], axis=1, inplace = True)

# boxplot all of the discrimination scores

discrimination.drop('SWANID', axis=1).plot(kind='box')

discrimination.disc0.describe()
discrimination.disc1.describe()
discrimination.disc2.describe()
discrimination.disc3.describe()

#############################################################
#                                                           #
#                   Perceived Stress                        #
#                                                           #
#############################################################

pstress_cols1 =['SWANID', 'CONTROL1', 'YOURWAY1', 'PILING1', 'ABILITY1']
pstress_cols2 =['SWANID', 'CONTROL2', 'YOURWAY2', 'PILING2', 'ABILITY2']
pstress_cols3 =['SWANID', 'CONTROL3', 'YOURWAY3', 'PILING3', 'ABILITY3']
pstress_cols4 =['SWANID', 'CONTROL4', 'YOURWAY4', 'PILING4', 'ABILITY4']
pstress_cols5 =['SWANID', 'CONTROL5', 'YOURWAY5', 'PILING5', 'ABILITY5']

cross_pstress = cross[['SWANID', 'P_STRESS']]
cross_pstress.rename(columns={'P_STRESS':'pstress0'}, inplace=True)

visit01_pstress = visit01[pstress_cols1]
visit02_pstress = visit02[pstress_cols2]
visit03_pstress = visit03[pstress_cols3]
visit04_pstress = visit04[pstress_cols4]
visit05_pstress = visit05[pstress_cols5]

# replacing null values

cross_pstress.replace(' ',np.nan,inplace=True)
visit01_pstress.replace(' ',np.nan,inplace=True)
visit02_pstress.replace(' ',np.nan,inplace=True)
visit03_pstress.replace(' ',np.nan,inplace=True)
visit04_pstress.replace(' ',np.nan,inplace=True)
visit05_pstress.replace(' ',np.nan,inplace=True)

visit01_pstress.replace('-1',np.nan,inplace=True)
visit02_pstress.replace('-1',np.nan,inplace=True)
visit03_pstress.replace('-1',np.nan,inplace=True)
visit04_pstress.replace('-1',np.nan,inplace=True)
visit05_pstress.replace('-1',np.nan,inplace=True)

# changing type to float

cross_pstress['pstress0'] = cross_pstress['pstress0'].astype(float)
visit01_pstress[pstress_cols1[1:]] = visit01_pstress[pstress_cols1[1:]].astype(float)
visit02_pstress[pstress_cols2[1:]] = visit02_pstress[pstress_cols2[1:]].astype(float)
visit03_pstress[pstress_cols3[1:]] = visit03_pstress[pstress_cols3[1:]].astype(float)
visit04_pstress[pstress_cols4[1:]] = visit04_pstress[pstress_cols4[1:]].astype(float)
visit05_pstress[pstress_cols5[1:]] = visit05_pstress[pstress_cols5[1:]].astype(float)

# calculating pstress values

visit01_pstress['pstress1'] = visit01_pstress[pstress_cols1[1:]].sum(axis=1)
visit02_pstress['pstress2'] = visit02_pstress[pstress_cols2[1:]].sum(axis=1)
visit03_pstress['pstress3'] = visit03_pstress[pstress_cols3[1:]].sum(axis=1)
visit04_pstress['pstress4'] = visit04_pstress[pstress_cols4[1:]].sum(axis=1)
visit05_pstress['pstress5'] = visit05_pstress[pstress_cols5[1:]].sum(axis=1)

# Merging on SWANID 

pstress = pd.merge(cross_pstress, visit01_pstress)
pstress = pd.merge(pstress, visit02_pstress)
pstress = pd.merge(pstress, visit03_pstress)
pstress = pd.merge(pstress, visit04_pstress)
pstress = pd.merge(pstress, visit05_pstress)

# dropping extraneous columns 

pstress.drop(pstress[pstress_cols1[1:]], axis=1, inplace = True)
pstress.drop(pstress[pstress_cols2[1:]], axis=1, inplace = True)
pstress.drop(pstress[pstress_cols3[1:]], axis=1, inplace = True)
pstress.drop(pstress[pstress_cols4[1:]], axis=1, inplace = True)
pstress.drop(pstress[pstress_cols5[1:]], axis=1, inplace = True)

# boxplot all of the discrimination scores

pstress.drop('SWANID', axis=1).plot(kind='box')

pstress.pstress0.describe()

#############################################################
#                                                           #
#                       Hostility                           #
#                                                           #
#############################################################


hostility_cols = ['SWANID', 'TAKEORD0', 'BADLUCK0', 'ARGUMEN0', 'HONEST0', 'PROFIT0', 'NONECAR0', 'NOTRUST0', 'FRIENDS0', 'PUTOUT0', 'EXPERTS0', 'RIGHTS0', 'SEXBEHA0', 'GETAHEA0']

baseline_host = baseline[hostility_cols]

# fill in missing values
baseline_host.replace(' ',np.nan, inplace=True)
baseline_host.replace('-9',np.nan, inplace=True)
baseline_host.replace('-8',np.nan, inplace=True)
baseline_host.replace('-1',np.nan, inplace=True)

# and because in this data set 1 = False and 2 = True let's change that
baseline_host.replace('1','0', inplace=True)
baseline_host.replace('2', '1', inplace=True)

# making types float
baseline_host[hostility_cols[1:]] = baseline_host[hostility_cols[1:]].astype(float)

# adding the scores together
baseline_host.loc[:, 'hostility'] = baseline_host[hostility_cols[1:]].sum(axis=1)

baseline_host.hostility.describe()

baseline_host.drop(baseline_host[hostility_cols[1:]], axis = 1, inplace = True)

#############################################################
#                                                           #
#                          Race                             #
#                                                           #
#############################################################

race = cross[['SWANID','ETHNIC']]


#############################################################
#                                                           #
#                     Systolic BP                           #
#                                                           #
#############################################################

baseline_bp = baseline[['SWANID', 'SYSBP10', 'SYSBP20', 'SYSBP30']]

sysbp_cols0 = ['SWANID', 'SYSBP10', 'SYSBP20', 'SYSBP30']
baseline_bp2 = baseline[sysbp_cols0]

def sysbpcalc(data, name_cols, mean_name, score_name):
    data.replace(' ',np.nan,inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    data.loc[:, mean_name] = data[name_cols[1:]].mean(axis=1)
    SYSBP_75 = data[mean_name].quantile(.75)
    SYSBP_max = data[mean_name].max()
    data[score_name] = 0
    data.loc[data[mean_name].between(SYSBP_75, SYSBP_max), score_name] = 1
    
sysbpcalc(baseline_bp2, sysbp_cols0, 'sysbp_mean0', 'sysbp_sc0')


    

baseline_bp.isnull().sum()
baseline_bp.isnull().sum(axis=1)

# replace " " with NaN so that converting to float won't throw an error
baseline_bp.replace(' ',np.nan,inplace=True)

# convert to float
baseline_bp[['SYSBP10', 'SYSBP20', 'SYSBP30']] = baseline_bp[['SYSBP10','SYSBP20','SYSBP30']].astype(float)

# find mean of SYSBP
baseline_bp.loc[:, 'SYSBP_mean'] = baseline_bp[['SYSBP10', 'SYSBP20', 'SYSBP30']].mean(axis=1)

# finding 75% of SYSBP
SYSBP_75 = baseline_bp.SYSBP_mean.quantile(.75)
SYSBP_max = baseline_bp.SYSBP_mean.max()

# initialize with 0
baseline_bp['SYSBP_sc'] = 0

# anything within 75% to max of SYSBP given a score of 1
baseline_bp.loc[baseline_bp.SYSBP_mean.between(SYSBP_75, SYSBP_max), 'SYSBP_sc'] = 1