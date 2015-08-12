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
visit06 = pd.read_table('06_Visit6.tsv', low_memory=False)
visit07 = pd.read_table('07_Visit7.tsv', low_memory=False)

# I could have probably made everything run easier with some
# complicated for-loop, but I chose to keep it simple and easy
# for at least me to understand

#############################################################
#                                                           #
#                   Discrimination                          #
#                                                           #
#############################################################

## Baseline, Visits 1-3, 7 only exist

def discfx(data, name_cols, mean_name):
    # replace survey null values with NaN
    data.replace(' ', np.nan, inplace=True)
    data.replace('-9', np.nan, inplace=True)
    data.replace('-7', np.nan, inplace=True)
    data.replace('-1', np.nan, inplace=True)
    # convert type to float for value columns
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    # adding the mean column = mean of all value columns
    data.loc[:, mean_name] = data[name_cols[1:]].mean(axis=1)
    # remove all columns except SWANID and disc score
    data.drop(data[name_cols[1:]],axis=1,inplace=True)

disc_cols0 = ['SWANID', 'COURTES0', 'RESPECT0', 'POORSER0', 'NOTSMAR0', 'AFRAIDO0', 'DISHONS0', 'BETTER0', 'INSULTE0', 'HARASSE0', 'IGNORED0']
disc_cols1 = ['SWANID', 'COURTES1', 'RESPECT1', 'POORSER1', 'NOTSMAR1', 'AFRAIDO1', 'DISHONS1', 'BETTER1', 'INSULTE1', 'HARASSE1', 'IGNORED1']
disc_cols2 = ['SWANID', 'COURTES2', 'RESPECT2', 'POORSER2', 'NOTSMAR2', 'AFRAIDO2', 'DISHONS2', 'BETTER2', 'INSULTE2', 'HARASSE2', 'IGNORED2']
disc_cols3 = ['SWANID', 'COURTES3', 'RESPECT3', 'POORSER3', 'NOTSMAR3', 'AFRAIDO3', 'DISHONS3', 'BETTER3', 'INSULTE3', 'HARASSE3', 'IGNORED3']
disc_cols7 = ['SWANID', 'COURTES7', 'RESPECT7', 'POORSER7', 'NOTSMAR7', 'AFRAIDO7', 'DISHONS7', 'BETTER7', 'INSULTE7', 'HARASSE7', 'IGNORED7']

baseline_disc = baseline[disc_cols0]
visit01_disc = visit01[disc_cols1]
visit02_disc = visit02[disc_cols2]
visit03_disc = visit03[disc_cols3]
visit07_disc = visit07[disc_cols7]

discfx(baseline_disc, disc_cols0, 'disc0')
discfx(visit01_disc, disc_cols1, 'disc1')
discfx(visit02_disc, disc_cols2, 'disc2')
discfx(visit03_disc, disc_cols3, 'disc3')
discfx(visit07_disc, disc_cols7, 'disc7')

discrimination = pd.merge(baseline_disc, visit01_disc, how='outer')
discrimination = pd.merge(discrimination, visit02_disc, how='outer')
discrimination = pd.merge(discrimination, visit03_disc, how='outer')
discrimination = pd.merge(discrimination, visit07_disc, how='outer')

disc_cols = ['disc0', 'disc1', 'disc2', 'disc3', 'disc7']
discrimination.loc[:, 'disc_total_mean'] = discrimination[disc_cols].mean(axis=1)

discrimination.disc0.replace(np.nan, discrimination.disc_total_mean, inplace=True)
discrimination.disc0.replace(np.nan, discrimination.disc0.mean(), inplace=True)

discrimination.disc1.replace(np.nan, discrimination.disc_total_mean, inplace=True)
discrimination.disc1.replace(np.nan, discrimination.disc1.mean(), inplace=True)

discrimination.drop(['disc2', 'disc3', 'disc7', 'disc_total_mean'], axis=1, inplace=True)

#############################################################
#                                                           #
#                   Perceived Stress                        #
#                                                           #
# Participants are asked to answer the following questions  #
# on a scale of 1-5, with 1 = Never and 5 = Very Often      #
# CONTROL = Felt unable to control important things in      #
#   your life?                                              #
# ABILITY = Felt confident about your ability to handle     #
#   personal problems?                                      #
# YOURWAY = Felt that things were going your way?           #
# PILING = Felt difficulties were piling so high that       #
#   could not overcome them?                                #
#                                                           #
# pstress = CONTROL + (6-ABILITY) + (6-YOURWAY) + PILING    #
#############################################################

def pstressfx(data, name_cols, score):
    # replace survey null values with NaN
    data.replace(' ', np.nan, inplace=True)
    data.replace('-9', np.nan, inplace=True)
    data.replace('-7', np.nan, inplace=True)
    data.replace('-1', np.nan, inplace=True)
    # convert type to float for value columns
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    # convert YOURWAY and ABILITY
    data[name_cols[2:3]] = 6 - data[name_cols[2:3]]
    data[name_cols[4:5]] = 6 - data[name_cols[4:5]]    
    # adding the sum column = sum of all cols
    data[score] = data[name_cols[1:]].sum(axis=1)
    data.replace(0, np.nan, inplace=True)
    # remove all cols except SWANID and pstress score
    data.drop(data[name_cols[1:]], axis=1, inplace=True)

pstress_cols1 =['SWANID', 'CONTROL1', 'YOURWAY1', 'PILING1', 'ABILITY1']
pstress_cols2 =['SWANID', 'CONTROL2', 'YOURWAY2', 'PILING2', 'ABILITY2']
pstress_cols3 =['SWANID', 'CONTROL3', 'YOURWAY3', 'PILING3', 'ABILITY3']
pstress_cols4 =['SWANID', 'CONTROL4', 'YOURWAY4', 'PILING4', 'ABILITY4']
pstress_cols5 =['SWANID', 'CONTROL5', 'YOURWAY5', 'PILING5', 'ABILITY5']
pstress_cols6 =['SWANID', 'CONTROL6', 'YOURWAY6', 'PILING6', 'ABILITY6']
pstress_cols7 =['SWANID', 'CONTROL7', 'YOURWAY7', 'PILING7', 'ABILITY7']

cross_pstress = cross[['SWANID', 'P_STRESS']]
cross_pstress.rename(columns={'P_STRESS':'pstress0'}, inplace=True)

visit01_pstress = visit01[pstress_cols1]
visit02_pstress = visit02[pstress_cols2]
visit03_pstress = visit03[pstress_cols3]
visit04_pstress = visit04[pstress_cols4]
visit05_pstress = visit05[pstress_cols5]
visit06_pstress = visit06[pstress_cols6]
visit07_pstress = visit07[pstress_cols7]

# cleaning cross-sectional data set
cross_pstress.replace(' ',np.nan,inplace=True) # filling ' ' with NaN
cross_pstress['pstress0'] = cross_pstress['pstress0'].astype(float) # changing type to float

# cleaning all other data
pstressfx(visit01_pstress, pstress_cols1, 'pstress01')
pstressfx(visit02_pstress, pstress_cols2, 'pstress02')
pstressfx(visit03_pstress, pstress_cols3, 'pstress03')
pstressfx(visit04_pstress, pstress_cols4, 'pstress04')
pstressfx(visit05_pstress, pstress_cols5, 'pstress05')
pstressfx(visit06_pstress, pstress_cols6, 'pstress06')
pstressfx(visit07_pstress, pstress_cols7, 'pstress07')

# Merging on SWANID 

pstress = pd.merge(cross_pstress, visit01_pstress, how='outer')
pstress = pd.merge(pstress, visit02_pstress, how='outer')
pstress = pd.merge(pstress, visit03_pstress, how='outer')
pstress = pd.merge(pstress, visit04_pstress, how='outer')
pstress = pd.merge(pstress, visit05_pstress, how='outer')
pstress = pd.merge(pstress, visit06_pstress, how='outer')
pstress = pd.merge(pstress, visit07_pstress, how='outer')

pstress_cols = ['pstress0', 'pstress01', 'pstress02', 'pstress03', 'pstress04', 'pstress05', 'pstress06', 'pstress07']

# adding an average pstress score over the years
pstress['pstress_avg'] = pstress[pstress_cols].mean(axis=1)

pstress_expl = pstress.copy()

pstress.pstress0.replace(np.nan, pstress.pstress_avg, inplace=True)
pstress.pstress0.replace(np.nan, pstress.pstress0.mean(), inplace=True)

pstress.pstress01.replace(np.nan, pstress.pstress_avg, inplace=True)
pstress.pstress01.replace(np.nan, pstress.pstress01.mean(), inplace=True)

pstress = pstress[['SWANID', 'pstress0', 'pstress01']]

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

# can't use an average from the user with only 1 set of data
# use most frequent
from sklearn.preprocessing import Imputer
imp = Imputer(strategy='most_frequent', axis=1)
baseline_host['hostility'] = imp.fit_transform(baseline_host.hostility).T

baseline_host.drop(baseline_host[hostility_cols[1:]], axis = 1, inplace = True)

hostility = baseline_host

#############################################################
#                                                           #
#                     Systolic BP                           #
#                                                           #
#############################################################

def sysbpcalc(data, name_cols, mean_name, score_name):
    # replace null values
    data.replace(' ',np.nan,inplace=True)
    # change to float type
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    # create mean column = average of sys bp measures
    data.loc[:, mean_name] = data[name_cols[1:]].mean(axis=1)
    data.drop(data[name_cols[1:]], axis=1, inplace=True)

sysbp_cols0 = ['SWANID', 'SYSBP10', 'SYSBP20', 'SYSBP30']
sysbp_cols1 = ['SWANID', 'SYSBP11', 'SYSBP21']
sysbp_cols2 = ['SWANID', 'SYSBP12', 'SYSBP22']
sysbp_cols3 = ['SWANID', 'SYSBP13', 'SYSBP23']
sysbp_cols4 = ['SWANID', 'SYSBP14', 'SYSBP24']
sysbp_cols5 = ['SWANID', 'SYSBP15', 'SYSBP25']
sysbp_cols6 = ['SWANID', 'SYSBP16', 'SYSBP26']
sysbp_cols7 = ['SWANID', 'SYSBP17', 'SYSBP27']

baseline_sysbp = baseline[sysbp_cols0]
visit01_sysbp = visit01[sysbp_cols1]
visit02_sysbp = visit02[sysbp_cols2]
visit03_sysbp = visit03[sysbp_cols3]
visit04_sysbp = visit04[sysbp_cols4]
visit05_sysbp = visit05[sysbp_cols5]
visit06_sysbp = visit06[sysbp_cols6]
visit07_sysbp = visit07[sysbp_cols7]

sysbpcalc(baseline_sysbp, sysbp_cols0, 'sysbp_mean0', 'sysbp_sc0')
sysbpcalc(visit01_sysbp, sysbp_cols1, 'sysbp_mean1', 'sysbp_sc1')
sysbpcalc(visit02_sysbp, sysbp_cols2, 'sysbp_mean2', 'sysbp_sc2')
sysbpcalc(visit03_sysbp, sysbp_cols3, 'sysbp_mean3', 'sysbp_sc3')
sysbpcalc(visit04_sysbp, sysbp_cols4, 'sysbp_mean4', 'sysbp_sc4')
sysbpcalc(visit05_sysbp, sysbp_cols5, 'sysbp_mean5', 'sysbp_sc5')
sysbpcalc(visit06_sysbp, sysbp_cols6, 'sysbp_mean6', 'sysbp_sc6')
sysbpcalc(visit07_sysbp, sysbp_cols7, 'sysbp_mean7', 'sysbp_sc7')

sysbp = pd.merge(baseline_sysbp, visit01_sysbp, how='outer')
sysbp = pd.merge(sysbp, visit02_sysbp, how='outer')
sysbp = pd.merge(sysbp, visit03_sysbp, how='outer')
sysbp = pd.merge(sysbp, visit04_sysbp, how='outer')
sysbp = pd.merge(sysbp, visit05_sysbp, how='outer')
sysbp = pd.merge(sysbp, visit06_sysbp, how='outer')
sysbp = pd.merge(sysbp, visit07_sysbp, how='outer')

sysbp_means = ['sysbp_mean0', 'sysbp_mean1', 'sysbp_mean2', 'sysbp_mean3', 'sysbp_mean4', 'sysbp_mean5', 'sysbp_mean6', 'sysbp_mean7']
sysbp_visits_means = ['sysbp_mean5', 'sysbp_mean7']

sysbp.loc[:, 'sys_total_mean'] = sysbp[sysbp_means].mean(axis=1)
sysbp.loc[:, 'sys_visits_mean'] = sysbp[sysbp_visits_means].mean(axis=1)

sysbp.sysbp_mean0.replace(np.nan, sysbp.sys_total_mean, inplace=True)
sysbp.sysbp_mean0.replace(np.nan, sysbp.sysbp_mean0.mean(), inplace=True)

sysbp.sysbp_mean1.replace(np.nan, sysbp.sys_total_mean, inplace=True)
sysbp.sysbp_mean1.replace(np.nan, sysbp.sysbp_mean1.mean(), inplace=True)

sysbp.sysbp_mean6.replace(np.nan, sysbp.sys_visits_mean, inplace=True)
sysbp.sysbp_mean6.replace(np.nan, sysbp.sys_total_mean, inplace=True)


#############################################################
#                                                           #
#                     Diastolic BP                          #
#                                                           #
#############################################################

def diabpcalc(data, name_cols, mean_name, score_name):
    # replace null values
    data.replace(' ',np.nan,inplace=True)
    # change to float type
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    # create mean column = average of dia bp measures
    data.loc[:, mean_name] = data[name_cols[1:]].mean(axis=1)   
    data.drop(data[name_cols[1:]], axis=1, inplace=True)

diabp_cols0 = ['SWANID', 'DIABP10', 'DIABP20', 'DIABP30']
diabp_cols1 = ['SWANID', 'DIABP11', 'DIABP21']
diabp_cols2 = ['SWANID', 'DIABP12', 'DIABP22']
diabp_cols3 = ['SWANID', 'DIABP13', 'DIABP23']
diabp_cols4 = ['SWANID', 'DIABP14', 'DIABP24']
diabp_cols5 = ['SWANID', 'DIABP15', 'DIABP25']
diabp_cols6 = ['SWANID', 'DIABP16', 'DIABP26']
diabp_cols7 = ['SWANID', 'DIABP17', 'DIABP27']

baseline_diabp = baseline[diabp_cols0]
visit01_diabp = visit01[diabp_cols1]
visit02_diabp = visit02[diabp_cols2]
visit03_diabp = visit03[diabp_cols3]
visit04_diabp = visit04[diabp_cols4]
visit05_diabp = visit05[diabp_cols5]
visit06_diabp = visit06[diabp_cols6]
visit07_diabp = visit07[diabp_cols7]

diabpcalc(baseline_diabp, diabp_cols0, 'diabp_mean0', 'diabp_sc0')
diabpcalc(visit01_diabp, diabp_cols1, 'diabp_mean1', 'diabp_sc1')
diabpcalc(visit02_diabp, diabp_cols2, 'diabp_mean2', 'diabp_sc2')
diabpcalc(visit03_diabp, diabp_cols3, 'diabp_mean3', 'diabp_sc3')
diabpcalc(visit04_diabp, diabp_cols4, 'diabp_mean4', 'diabp_sc4')
diabpcalc(visit05_diabp, diabp_cols5, 'diabp_mean5', 'diabp_sc5')
diabpcalc(visit06_diabp, diabp_cols6, 'diabp_mean6', 'diabp_sc6')
diabpcalc(visit07_diabp, diabp_cols7, 'diabp_mean7', 'diabp_sc7')

diabp = pd.merge(baseline_diabp, visit01_diabp, how='outer')
diabp = pd.merge(diabp, visit02_diabp, how='outer')
diabp = pd.merge(diabp, visit03_diabp, how='outer')
diabp = pd.merge(diabp, visit04_diabp, how='outer')
diabp = pd.merge(diabp, visit05_diabp, how='outer')
diabp = pd.merge(diabp, visit06_diabp, how='outer')
diabp = pd.merge(diabp, visit07_diabp, how='outer')

diabp_means = ['diabp_mean0', 'diabp_mean1', 'diabp_mean2', 'diabp_mean3', 'diabp_mean4', 'diabp_mean5', 'diabp_mean6', 'diabp_mean7']
diabp_visits_means = ['diabp_mean5', 'diabp_mean7']

diabp.loc[:, 'dia_total_mean'] = diabp[diabp_means].mean(axis=1)
diabp.loc[:, 'dia_visits_mean'] = diabp[diabp_visits_means].mean(axis=1)

diabp.diabp_mean0.replace(np.nan, diabp.dia_total_mean, inplace=True)
diabp.diabp_mean0.replace(np.nan, diabp.diabp_mean0.mean(), inplace=True)

diabp.diabp_mean1.replace(np.nan, diabp.dia_total_mean, inplace=True)
diabp.diabp_mean1.replace(np.nan, diabp.diabp_mean1.mean(), inplace=True)

diabp.diabp_mean6.replace(np.nan, diabp.dia_visits_mean, inplace=True)
diabp.diabp_mean6.replace(np.nan, diabp.dia_total_mean, inplace=True)

#############################################################
#                                                           #
#                  Metabolic Measures 1                     #
# Includes: cholesterol, HDL, triglycerides, and glucose    #
#                                                           #
#############################################################

# metabolic measures are split in anticipation of having to do some
# imputation for certain metabolic markers

def cleanfx(data, name_cols):
    data.replace(' ', np.nan, inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)   

metab1_cols0 = ['SWANID', 'CHOLRES0', 'HDLRESU0', 'TRIGRES0', 'GLUCRES0']
metab1_cols1 = ['SWANID', 'CHOLRES1', 'HDLRESU1', 'TRIGRES1', 'GLUCRES1']
#metab1_cols2 = ['SWANID', 'CHOLRES2', 'HDLRESU2', 'TRIGRES2', 'GLUCRES2'] <-- never collected
metab1_cols3 = ['SWANID', 'CHOLRES3', 'HDLRESU3', 'TRIGRES3', 'GLUCRES3']
metab1_cols4 = ['SWANID', 'CHOLRES4', 'HDLRESU4', 'TRIGRES4', 'GLUCRES4']
metab1_cols5 = ['SWANID', 'CHOLRES5', 'HDLRESU5', 'TRIGRES5', 'GLUCRES5']
metab1_cols6 = ['SWANID', 'CHOLRES6', 'HDLRESU6', 'TRIGRES6', 'GLUCRES6']
metab1_cols7 = ['SWANID', 'CHOLRES7', 'HDLRESU7', 'TRIGRES7', 'GLUCRES7']

baseline_metab1 = baseline[metab1_cols0]
visit01_metab1 = visit01[metab1_cols1]
#visit02_metab1 = visit02[metab1_cols2]
visit03_metab1 = visit03[metab1_cols3]
visit04_metab1 = visit04[metab1_cols4]
visit05_metab1 = visit05[metab1_cols5]
visit06_metab1 = visit06[metab1_cols6]
visit07_metab1 = visit07[metab1_cols7]

cleanfx(baseline_metab1, metab1_cols0)
cleanfx(visit01_metab1, metab1_cols1)
#cleanfx(visit02_metab1, metab1_cols2)
cleanfx(visit03_metab1, metab1_cols3)
cleanfx(visit04_metab1, metab1_cols4)
cleanfx(visit05_metab1, metab1_cols5)
cleanfx(visit06_metab1, metab1_cols6)
cleanfx(visit07_metab1, metab1_cols7)

metab1 = pd.merge(baseline_metab1, visit01_metab1, how='outer')
metab1 = pd.merge(metab1, visit03_metab1, how='outer')
metab1 = pd.merge(metab1, visit04_metab1, how='outer')
metab1 = pd.merge(metab1, visit05_metab1, how='outer')
metab1 = pd.merge(metab1, visit06_metab1, how='outer')
metab1 = pd.merge(metab1, visit07_metab1, how='outer')

choles_mean_cols = ['CHOLRES0', 'CHOLRES1', 'CHOLRES3', 'CHOLRES4', 'CHOLRES5', 'CHOLRES6', 'CHOLRES7']
hdl_mean_cols = ['HDLRESU0', 'HDLRESU1', 'HDLRESU3', 'HDLRESU4', 'HDLRESU5', 'HDLRESU6', 'HDLRESU7']
tri_mean_cols = ['TRIGRES0', 'TRIGRES1', 'TRIGRES3', 'TRIGRES4', 'TRIGRES5', 'TRIGRES6', 'TRIGRES7']
glu_mean_cols = ['GLUCRES0', 'GLUCRES1', 'GLUCRES3', 'GLUCRES4', 'GLUCRES5', 'GLUCRES6', 'GLUCRES7']

choles_visit_mean_cols = ['CHOLRES5', 'CHOLRES7']
hdl_visit_mean_cols = ['HDLRESU5', 'HDLRESU7']
tri_visit_mean_cols = ['TRIGRES5', 'TRIGRES7']
glu_visit_mean_cols = ['GLUCRES5', 'GLUCRES7']

metab1.loc[:, 'choles_mean'] = metab1[choles_mean_cols].mean(axis=1)
metab1.loc[:, 'hdl_mean'] = metab1[hdl_mean_cols].mean(axis=1)
metab1.loc[:, 'tri_mean'] = metab1[tri_mean_cols].mean(axis=1)
metab1.loc[:, 'gluc_mean'] = metab1[glu_mean_cols].mean(axis=1)

metab1.loc[:, 'choles_visits_mean'] = metab1[choles_visit_mean_cols].mean(axis=1)
metab1.loc[:, 'hdl_visits_mean'] = metab1[hdl_visit_mean_cols].mean(axis=1)
metab1.loc[:, 'tri_visits_mean'] = metab1[tri_visit_mean_cols].mean(axis=1)
metab1.loc[:, 'gluc_visits_mean'] = metab1[glu_visit_mean_cols].mean(axis=1)

metab1.CHOLRES0.replace(np.nan, metab1.choles_mean, inplace=True)
metab1.CHOLRES0.replace(np.nan, metab1.CHOLRES0.mean(), inplace=True)

metab1.HDLRESU0.replace(np.nan, metab1.hdl_mean, inplace=True)
metab1.HDLRESU0.replace(np.nan, metab1.HDLRESU0.mean(), inplace=True)

metab1.TRIGRES0.replace(np.nan, metab1.tri_mean, inplace=True)
metab1.TRIGRES0.replace(np.nan, metab1.TRIGRES0.mean(), inplace=True)

metab1.GLUCRES0.replace(np.nan, metab1.gluc_mean, inplace=True)
metab1.GLUCRES0.replace(np.nan, metab1.GLUCRES0.mean(), inplace=True)

metab1.CHOLRES1.replace(np.nan, metab1.choles_mean, inplace=True)
metab1.CHOLRES1.replace(np.nan, metab1.CHOLRES1.mean(), inplace=True)

metab1.HDLRESU1.replace(np.nan, metab1.hdl_mean, inplace=True)
metab1.HDLRESU1.replace(np.nan, metab1.HDLRESU1.mean(), inplace=True)

metab1.TRIGRES1.replace(np.nan, metab1.tri_mean, inplace=True)
metab1.TRIGRES1.replace(np.nan, metab1.TRIGRES1.mean(), inplace=True)

metab1.GLUCRES1.replace(np.nan, metab1.gluc_mean, inplace=True)
metab1.GLUCRES1.replace(np.nan, metab1.GLUCRES1.mean(), inplace=True)

metab1.CHOLRES6.replace(np.nan, metab1.choles_visits_mean, inplace=True)
metab1.CHOLRES6.replace(np.nan, metab1.choles_mean, inplace=True)

metab1.HDLRESU6.replace(np.nan, metab1.hdl_visits_mean, inplace=True)
metab1.HDLRESU6.replace(np.nan, metab1.hdl_mean, inplace=True)

metab1.TRIGRES6.replace(np.nan, metab1.tri_visits_mean, inplace=True)
metab1.TRIGRES6.replace(np.nan, metab1.tri_mean, inplace=True)

metab1.GLUCRES6.replace(np.nan, metab1.gluc_visits_mean, inplace=True)
metab1.GLUCRES6.replace(np.nan, metab1.gluc_mean, inplace=True)

#############################################################
#                                                           #
#                  Metabolic Measures 2                     #
# Includes: BMI, waist to hip ratio                         #
#                                                           #
#############################################################

metab2_cols0 = ['SWANID', 'BMI0', 'WAIST0', 'HIP0']
metab2_cols1 = ['SWANID', 'BMI1', 'WAIST1', 'HIP1']
metab2_cols2 = ['SWANID', 'BMI2', 'WAIST2', 'HIP2']
metab2_cols3 = ['SWANID', 'BMI3', 'WAIST3', 'HIP3']
metab2_cols4 = ['SWANID', 'BMI4', 'WAIST4', 'HIP4']
metab2_cols5 = ['SWANID', 'BMI5', 'WAIST5', 'HIP5']
metab2_cols6 = ['SWANID', 'BMI6', 'WAIST6', 'HIP6']
metab2_cols7 = ['SWANID', 'BMI7', 'WAIST7', 'HIP7']

baseline_metab2 = baseline[metab2_cols0]
visit01_metab2 = visit01[metab2_cols1]
visit02_metab2 = visit02[metab2_cols2]
visit03_metab2 = visit03[metab2_cols3]
visit04_metab2 = visit04[metab2_cols4]
visit05_metab2 = visit05[metab2_cols5]
visit06_metab2 = visit06[metab2_cols6]
visit07_metab2 = visit07[metab2_cols7]

cleanfx(baseline_metab2, metab2_cols0)
cleanfx(visit01_metab2, metab2_cols1)
cleanfx(visit02_metab2, metab2_cols2)
cleanfx(visit03_metab2, metab2_cols3)
cleanfx(visit04_metab2, metab2_cols4)
cleanfx(visit05_metab2, metab2_cols5)
cleanfx(visit06_metab2, metab2_cols6)
cleanfx(visit07_metab2, metab2_cols7)

metab2 = pd.merge(baseline_metab2, visit01_metab2, how='outer')
metab2 = pd.merge(metab2, visit02_metab2, how='outer')
metab2 = pd.merge(metab2, visit03_metab2, how='outer')
metab2 = pd.merge(metab2, visit04_metab2, how='outer')
metab2 = pd.merge(metab2, visit05_metab2, how='outer')
metab2 = pd.merge(metab2, visit06_metab2, how='outer')
metab2 = pd.merge(metab2, visit07_metab2, how='outer')

bmi_mean_cols = ['BMI0', 'BMI1', 'BMI2', 'BMI3', 'BMI4', 'BMI5', 'BMI6', 'BMI7']
waist_mean_cols = ['WAIST0', 'WAIST1', 'WAIST2', 'WAIST3', 'WAIST4', 'WAIST5', 'WAIST6', 'WAIST7']
hip_mean_cols = ['HIP0', 'HIP1', 'HIP2', 'HIP3', 'HIP4', 'HIP5', 'HIP6', 'HIP7']

bmi_visit_mean_cols = ['BMI5', 'BMI7']
waist_visit_mean_cols = ['WAIST5', 'WAIST7']
hip_visit_mean_cols = ['HIP5', 'HIP7']

metab2.loc[:, 'bmi_mean'] = metab2[bmi_mean_cols].mean(axis=1)
metab2.loc[:, 'waist_mean'] = metab2[waist_mean_cols].mean(axis=1)
metab2.loc[:, 'hip_mean'] = metab2[hip_mean_cols].mean(axis=1)

metab2.loc[:, 'bmi_visits_mean'] = metab2[bmi_visit_mean_cols].mean(axis=1)
metab2.loc[:, 'waist_visits_mean'] = metab2[waist_visit_mean_cols].mean(axis=1)
metab2.loc[:, 'hip_visits_mean'] = metab2[hip_visit_mean_cols].mean(axis=1)

metab2.BMI6.replace(np.nan, metab2.bmi_visits_mean, inplace=True)
metab2.BMI6.replace(np.nan, metab2.bmi_mean, inplace=True)
metab2.BMI6.replace(np.nan, metab2.BMI6.mean(), inplace=True)

metab2.BMI1.replace(np.nan, metab2.bmi_mean, inplace=True)
metab2.BMI1.replace(np.nan, metab2.BMI1.mean(), inplace=True)

metab2.BMI0.replace(np.nan, metab2.bmi_mean, inplace=True)
metab2.BMI0.replace(np.nan, metab2.BMI0.mean(), inplace=True)

metab2.WAIST6.replace(np.nan, metab2.waist_visits_mean, inplace=True)
metab2.WAIST6.replace(np.nan, metab2.waist_mean, inplace=True)
metab2.WAIST6.replace(np.nan, metab2.WAIST6.mean(), inplace=True)

metab2.WAIST1.replace(np.nan, metab2.waist_mean, inplace=True)
metab2.WAIST1.replace(np.nan, metab2.WAIST1.mean(), inplace=True)

metab2.WAIST0.replace(np.nan, metab2.waist_mean, inplace=True)
metab2.WAIST0.replace(np.nan, metab2.WAIST0.mean(), inplace=True)

metab2.HIP6.replace(np.nan, metab2.hip_visits_mean, inplace=True)
metab2.HIP6.replace(np.nan, metab2.hip_mean, inplace=True)
metab2.HIP6.replace(np.nan, metab2.HIP6.mean(), inplace=True)

metab2.HIP1.replace(np.nan, metab2.hip_mean, inplace=True)
metab2.HIP1.replace(np.nan, metab2.HIP6.mean(), inplace=True)

metab2.HIP0.replace(np.nan, metab2.hip_mean, inplace=True)
metab2.HIP0.replace(np.nan, metab2.HIP0.mean(), inplace=True)

metab2['whratio0'] = metab2.WAIST0 / metab2.HIP0
metab2['whratio1'] = metab2.WAIST1 / metab2.HIP1
metab2['whratio6'] = metab2.WAIST6 / metab2.HIP6


#############################################################
#                                                           #
#                  Inflammatory/Neuro                       #
#                                                           #
#############################################################

inflno_cols0 = ['SWANID', 'CRPRESU0', 'FIBRESU0', 'DHAS0']
inflno_cols1 = ['SWANID', 'CRPRESU1', 'FIBRESU1', 'DHAS1']
inflno_cols2 = ['SWANID', 'CRPRESU2', 'FIBRESU2', 'DHAS2']
inflno_cols3 = ['SWANID', 'CRPRESU3', 'FIBRESU3', 'DHAS3']
inflno_cols4 = ['SWANID', 'CRPRESU4', 'DHAS4']
inflno_cols5 = ['SWANID', 'CRPRESU5', 'FIBRESU5', 'DHAS5']
inflno_cols6 = ['SWANID', 'CRPRESU6', 'DHAS6']
inflno_cols7 = ['SWANID', 'CRPRESU7', 'FIBRESU7', 'DHAS7']

baseline_inflno = baseline[inflno_cols0]
visit01_inflno = visit01[inflno_cols1]
#visit02_inflno = visit02[inflno_cols2] <-- never collected
visit03_inflno = visit03[inflno_cols3]
visit04_inflno = visit04[inflno_cols4]
visit05_inflno = visit05[inflno_cols5]
visit06_inflno = visit06[inflno_cols6]
visit07_inflno = visit07[inflno_cols7]

cleanfx(baseline_inflno, inflno_cols0)
cleanfx(visit01_inflno, inflno_cols1)
#cleanfx(visit02_inflno, inflno_cols2)
cleanfx(visit03_inflno, inflno_cols3)
cleanfx(visit04_inflno, inflno_cols4)
cleanfx(visit05_inflno, inflno_cols5)
cleanfx(visit06_inflno, inflno_cols6)
cleanfx(visit07_inflno, inflno_cols7)

inflno = pd.merge(baseline_inflno, visit01_inflno, how='outer')
#inflno = pd.merge(inflno, visit02_inflno, how='outer')
inflno = pd.merge(inflno, visit03_inflno, how='outer')
inflno = pd.merge(inflno, visit04_inflno, how='outer')
inflno = pd.merge(inflno, visit05_inflno, how='outer')
inflno = pd.merge(inflno, visit06_inflno, how='outer')
inflno = pd.merge(inflno, visit07_inflno, how='outer')

crp_mean_cols = ['CRPRESU0', 'CRPRESU1', 'CRPRESU3', 'CRPRESU4', 'CRPRESU5', 'CRPRESU6', 'CRPRESU7']
fib_mean_cols = ['FIBRESU0', 'FIBRESU1', 'FIBRESU3', 'FIBRESU5', 'FIBRESU7']
dha_mean_cols = ['DHAS0', 'DHAS1', 'DHAS3', 'DHAS4', 'DHAS5', 'DHAS6', 'DHAS7']

crp_visit_mean_cols = ['CRPRESU5', 'CRPRESU7']
fib_visit_mean_cols = ['FIBRESU5', 'FIBRESU7']
dha_visit_mean_cols = ['DHAS5', 'DHAS7']

inflno.loc[:, 'crp_mean'] = inflno[crp_mean_cols].mean(axis=1)
inflno.loc[:, 'fib_mean'] = inflno[fib_mean_cols].mean(axis=1)
inflno.loc[:, 'dha_mean'] = inflno[dha_mean_cols].mean(axis=1)
 
inflno.loc[:, 'crp_visits_mean'] = inflno[crp_visit_mean_cols].mean(axis=1)
inflno.loc[:, 'fib_visits_mean'] = inflno[fib_visit_mean_cols].mean(axis=1)
inflno.loc[:, 'dha_visits_mean'] = inflno[dha_visit_mean_cols].mean(axis=1)

inflno.CRPRESU6.replace(np.nan, inflno.crp_visits_mean, inplace=True)
inflno.CRPRESU6.replace(np.nan, inflno.crp_mean, inplace=True)

inflno['FIBRESU6'] = inflno.fib_visits_mean
inflno.FIBRESU6.replace(np.nan, inflno.fib_mean, inplace=True)

inflno.DHAS6.replace(np.nan, inflno.dha_visits_mean, inplace=True)
inflno.DHAS6.replace(np.nan, inflno.dha_mean, inplace=True)

inflno.CRPRESU0.replace(np.nan, inflno.crp_mean, inplace=True)
inflno.CRPRESU0.replace(np.nan, inflno.CRPRESU0.mean(), inplace=True)

inflno.FIBRESU0.replace(np.nan, inflno.fib_mean, inplace=True)
inflno.FIBRESU0.replace(np.nan, inflno.FIBRESU0.mean(), inplace=True)

inflno.DHAS0.replace(np.nan, inflno.dha_mean, inplace=True)
inflno.DHAS0.replace(np.nan, inflno.DHAS0.mean(), inplace=True)

inflno.CRPRESU1.replace(np.nan, inflno.crp_mean, inplace=True)
inflno.CRPRESU1.replace(np.nan, inflno.CRPRESU1.mean(), inplace=True)

inflno.FIBRESU1.replace(np.nan, inflno.fib_mean, inplace=True)
inflno.FIBRESU1.replace(np.nan, inflno.FIBRESU1.mean(), inplace=True)

inflno.DHAS1.replace(np.nan, inflno.dha_mean, inplace=True)
inflno.DHAS1.replace(np.nan, inflno.DHAS1.mean(), inplace=True)

#############################################################
#                                                           #
#             Calculating Allostatic Load                   #
#                                                           #
#############################################################

# sysbp
# diabp
# metab1
# metab2
# inflno

# hdl and dhas must be 25%

def allostaticfx(data, name_cols, score_name, cutoff):
    if cutoff == 75:
        marker_75 = data[name_cols].quantile(.75)
        marker_max = data[name_cols].max()
        data[score_name] = 0
        data.loc[data[name_cols].between(marker_75, marker_max), score_name] = 1
    else:
        marker_25 = data[name_cols].quantile(.25)
        marker_min = data[name_cols].min()
        data[score_name] = 0
        data.loc[data[name_cols].between(marker_min, marker_25), score_name] = 1

visits = ['0', '1', '6']
response_names = [[sysbp, 'sysbp_mean'], [diabp, 'diabp_mean'], [metab1, 'CHOLRES'], [metab1, 'HDLRESU'], [metab1, 'TRIGRES'], [metab1, 'GLUCRES'], [metab2, 'BMI'], [metab2, 'whratio'], [inflno, 'CRPRESU'], [inflno, 'FIBRESU'], [inflno, 'DHAS']]
allostatic = pd.DataFrame(sysbp[['SWANID']])

for x in visits:
    for y in range(11):
        data = response_names[y][0]
        name_cols = response_names[y][1] + x
        score_name = response_names[y][1] + '_score' + x
        if response_names[y][1] == 'HDLRESU' or response_names[y][1] == 'DHAS':
            cutoff = 25
        else:
            cutoff = 75
        allostaticfx(data, name_cols, score_name, cutoff)
        allostatic = pd.merge(allostatic, data[['SWANID', score_name]], how='outer')

baseline_response = []
visit01_response = []
visit06_response = []

for y in range(11):
    baseline_response.append(response_names[y][1] + '_score0')
    visit01_response.append(response_names[y][1] + '_score1')
    visit06_response.append(response_names[y][1] + '_score6')

allostatic['AL0'] = allostatic[baseline_response].sum(axis=1)
allostatic['AL1'] = allostatic[visit01_response].sum(axis=1)
allostatic['AL6'] = allostatic[visit06_response].sum(axis=1)

allostatic.isnull().sum()

AL = allostatic[['SWANID', 'AL0', 'AL1', 'AL6']].copy()
AL['change'] = AL.AL6 - AL.AL0

#############################################################
#                                                           #
#          Education, Race, Marital Status                  #
#                                                           #
#############################################################

demo = cross[['SWANID', 'ETHNIC', 'DEGREE', 'MARITALGP']]
demo.replace(' ', np.nan, inplace=True)

demo.dropna(subset = ['ETHNIC'], inplace=True)

demo['ETHNIC'] = demo.ETHNIC.map({'1':'AfAm', '8':'0Asian', '9':'0Asian', '10':'White', '13':'Hispanic'})
demo['DEGREE'] = demo.DEGREE.map({'1':1, '2':2, '3':3, '4':4, '5':5})
demo['MARITALGP'] = demo.MARITALGP.map({'1':0, '2':1, '3':0, '4':0})

ethnic_dummies = pd.get_dummies(demo.ETHNIC, prefix='Race').iloc[:, 1:]
demo = pd.concat([demo, ethnic_dummies], axis=1)

visit01_marital = visit01[['SWANID', 'MARITAL1']]
visit01_marital['MARITAL1'] = visit01_marital.MARITAL1.map({'1':0, '2':1, '3':0, '4':0, '5':0, ' ':2, '-9':2, '-8':2})
visit01_marital.replace(2, np.nan, inplace=True)

visit02_marital = visit02[['SWANID', 'MARITAL2']]
visit02_marital['MARITAL2'] = visit02_marital.MARITAL2.map({'1':0, '2':1, '3':0, '4':0, '5':0, ' ':2, '-9':2, '-8':2})
visit02_marital.replace(2, np.nan, inplace=True)

demo = pd.merge(demo, visit01_marital, how='outer')
demo = pd.merge(demo, visit02_marital, how='outer')

#############################################################
#                                                           #
#                         Income                            #
#                                                           #
#############################################################

income = baseline[['SWANID', 'INCOME0']]
income = pd.merge(income, visit01[['SWANID', 'INCOME1']], how='outer')
income = pd.merge(income, visit02[['SWANID', 'INCOME2']], how='outer')

income.replace(' ', np.nan, inplace=True)
income.replace('-7', np.nan, inplace=True)
income.replace('-8', np.nan, inplace=True)
income.replace('-9', np.nan, inplace=True)

income.dropna(subset = (['INCOME0', 'INCOME1', 'INCOME2']))

income['INCOME0'] = income.INCOME0.map({'1':1, '2':2, '3':3, '4':4})
income['INCOME1'] = income.INCOME1.map({'1':1, '2':2, '3':3, '4':4})
income['INCOME2'] = income.INCOME2.map({'1':1, '2':2, '3':3, '4':4})

income.INCOME0.replace(np.nan, income.INCOME1, inplace = True)
income.INCOME0.replace(np.nan, income.INCOME2, inplace = True)

income.INCOME1.replace(np.nan, income.INCOME0, inplace= True)
income.INCOME1.replace(np.nan, income.INCOME2, inplace= True)

#############################################################
#                                                           #
#                           Age                             #
#                                                           #
#############################################################

baseline_age = baseline[['SWANID', 'AGE0']]
visit01_age = visit01[['SWANID', 'AGE1']]

baseline_age.replace(' ', np.nan, inplace=True)
visit01_age.replace(' ', np.nan, inplace=True)

age = pd.merge(baseline_age, visit01_age, how='outer')

age[['AGE0', 'AGE1']] = age[['AGE0', 'AGE1']].astype(float)

age.AGE0.replace(np.nan, age.AGE1 - 2, inplace = True)
age.AGE0.replace(np.nan, age.AGE0.mean(), inplace = True)

age.AGE1.replace(np.nan, age.AGE0 + 2, inplace = True)
age.AGE1.replace(np.nan, age.AGE1.mean(), inplace = True)

#############################################################
#                                                           #
#                  Menopause Status                         #
#                                                           #
#############################################################
 
baseline_meno = baseline[['SWANID', 'STATUS0']]
visit01_meno = visit01[['SWANID', 'STATUS1']]
visit02_meno = visit02[['SWANID', 'STATUS2']]

menopause = pd.merge(baseline_meno, visit01_meno, how='outer')
menopause = pd.merge(menopause, visit02_meno, how='outer')

menopause.replace(' ', np.nan, inplace=True)

menopause['STATUS1'] = menopause.STATUS1.map({'1':3, '2':3, '3':2, '4':2, '5':1, '6':1, '7':0})
menopause['STATUS2'] = menopause.STATUS2.map({'1':3, '2':3, '3':2, '4':2, '5':1, '6':1, '7':0})

# 3 = post
# 2 = peri
# 1 = pre
# 0 = hormone therapy use

menopause.STATUS0.replace(np.nan, menopause.STATUS1, inplace=True)
menopause.STATUS0.replace(np.nan, menopause.STATUS2, inplace=True)

menopause.STATUS1.replace(np.nan, menopause.STATUS0, inplace=True)
menopause.STATUS1.replace(np.nan, menopause.STATUS2, inplace=True)

#############################################################
#                                                           #
#                 Putting together Features                 #
#                                                           #
#############################################################

features = pd.merge(demo, age)
features = pd.merge(features, income)
features = pd.merge(features, menopause)
features = pd.merge(features, discrimination)
features = pd.merge(features, pstress)
features = pd.merge(features, hostility)

# imputing missing values from the demo data set
# waited until combining all of the features to get the correct sample size

features.isnull().sum()

features['DEGREE'] = imp.fit_transform(features.DEGREE).T
features['MARITALGP'] = imp.fit_transform(features.MARITALGP).T
features['MARITAL1'] = imp.fit_transform(features.MARITAL1).T
features['INCOME0'] = imp.fit_transform(features.INCOME0).T
features['INCOME1'] = imp.fit_transform(features.INCOME1).T
features['STATUS0'] = imp.fit_transform(features.STATUS0).T
features['STATUS1'] = imp.fit_transform(features.STATUS1).T

features.drop(['MARITAL2', 'INCOME2', 'STATUS2'], axis=1, inplace=True)

data = pd.merge(features, AL)

features.to_csv('features.csv', index=False)
AL.to_csv('AL.csv', index=False)
data.to_csv('data.csv', index=False)
