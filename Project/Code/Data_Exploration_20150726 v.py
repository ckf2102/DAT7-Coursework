
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
#                     Systolic BP                           #
#                                                           #
#############################################################

def sysbpcalc(data, name_cols, mean_name, score_name):
    data.replace(' ',np.nan,inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    data.loc[:, mean_name] = data[name_cols[1:]].mean(axis=1)
    SYSBP_75 = data[mean_name].quantile(.75)
    SYSBP_max = data[mean_name].max()
    data[score_name] = 0
    data.loc[data[mean_name].between(SYSBP_75, SYSBP_max), score_name] = 1
    data.drop(data[name_cols[1:]],axis=1,inplace=True)

sysbp_cols0 = ['SWANID', 'SYSBP10', 'SYSBP20', 'SYSBP30']
sysbp_cols1 = ['SWANID', 'SYSBP11', 'SYSBP21']
sysbp_cols2 = ['SWANID', 'SYSBP12', 'SYSBP22']
sysbp_cols3 = ['SWANID', 'SYSBP13', 'SYSBP23']
sysbp_cols4 = ['SWANID', 'SYSBP14', 'SYSBP24']
sysbp_cols5 = ['SWANID', 'SYSBP15', 'SYSBP25']

baseline_sysbp = baseline[sysbp_cols0]
visit01_sysbp = visit01[sysbp_cols1]
visit02_sysbp = visit02[sysbp_cols2]
visit03_sysbp = visit03[sysbp_cols3]
visit04_sysbp = visit04[sysbp_cols4]
visit05_sysbp = visit05[sysbp_cols5]

sysbpcalc(baseline_sysbp, sysbp_cols0, 'sysbp_mean0', 'sysbp_sc0')
sysbpcalc(visit01_sysbp, sysbp_cols1, 'sysbp_mean1', 'sysbp_sc1')
sysbpcalc(visit02_sysbp, sysbp_cols2, 'sysbp_mean2', 'sysbp_sc2')
sysbpcalc(visit03_sysbp, sysbp_cols3, 'sysbp_mean3', 'sysbp_sc3')
sysbpcalc(visit04_sysbp, sysbp_cols4, 'sysbp_mean4', 'sysbp_sc4')
sysbpcalc(visit05_sysbp, sysbp_cols5, 'sysbp_mean5', 'sysbp_sc5')

#############################################################
#                                                           #
#                     Diastolic BP                          #
#                                                           #
#############################################################

def diabpcalc(data, name_cols, mean_name, score_name):
    data.replace(' ',np.nan,inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    data.loc[:, mean_name] = data[name_cols[1:]].mean(axis=1)
    DIABP_75 = data[mean_name].quantile(.75)
    DIABP_max = data[mean_name].max()
    data[score_name] = 0
    data.loc[data[mean_name].between(DIABP_75, DIABP_max), score_name] = 1
    data.drop(data[name_cols[1:]],axis=1,inplace=True)

diabp_cols0 = ['SWANID', 'DIABP10', 'DIABP20', 'DIABP30']
diabp_cols1 = ['SWANID', 'DIABP11', 'DIABP21']
diabp_cols2 = ['SWANID', 'DIABP12', 'DIABP22']
diabp_cols3 = ['SWANID', 'DIABP13', 'DIABP23']
diabp_cols4 = ['SWANID', 'DIABP14', 'DIABP24']
diabp_cols5 = ['SWANID', 'DIABP15', 'DIABP25']

baseline_diabp = baseline[diabp_cols0]
visit01_diabp = visit01[diabp_cols1]
visit02_diabp = visit02[diabp_cols2]
visit03_diabp = visit03[diabp_cols3]
visit04_diabp = visit04[diabp_cols4]
visit05_diabp = visit05[diabp_cols5]

diabpcalc(baseline_diabp, diabp_cols0, 'diabp_mean0', 'diabp_sc0')
diabpcalc(visit01_diabp, diabp_cols1, 'diabp_mean1', 'diabp_sc1')
diabpcalc(visit02_diabp, diabp_cols2, 'diabp_mean2', 'diabp_sc2')
diabpcalc(visit03_diabp, diabp_cols3, 'diabp_mean3', 'diabp_sc3')
diabpcalc(visit04_diabp, diabp_cols4, 'diabp_mean4', 'diabp_sc4')
diabpcalc(visit05_diabp, diabp_cols5, 'diabp_mean5', 'diabp_sc5')

#############################################################
#                                                           #
#                  Metabolic Measures 1                     #
# Includes: cholesterol, HDL, triglycerides, and glucose    #
#                                                           #
#############################################################

"""
def diabpcalc(data, name_cols, mean_name, score_name):
    data.replace(' ',np.nan,inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    data.loc[:, mean_name] = data[name_cols[1:]].mean(axis=1)
    DIABP_75 = data[mean_name].quantile(.75)
    DIABP_max = data[mean_name].max()
    data[score_name] = 0
    data.loc[data[mean_name].between(DIABP_75, DIABP_max), score_name] = 1
    data.drop(data[name_cols[1:]],axis=1,inplace=True)
"""

def metab1(data, name_cols, numstr):
    data.replace(' ', np.nan, inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    # cholesterol
    cholest_75 = data[name_cols[1]].quantile(.75)
    cholest_max = data[name_cols[1]].max()
    data['cholest_sc' + numstr] = 0
    data.loc[data[name_cols[1]].between(cholest_75, cholest_max), 'cholest_sc' + numstr] = 1
    # hdl
    hdl_25 = data[name_cols[2]].quantile(.25)
    hdl_min = data[name_cols[2]].min()
    data['hdl_sc' + numstr] = 0
    data.loc[data[name_cols[2]].between(hdl_min, hdl_25), 'hdl_sc' + numstr] = 1
    # tri
    tri_75 = data[name_cols[3]].quantile(.75)
    tri_max = data[name_cols[3]].max()
    data['tri_sc' + numstr] = 0
    data.loc[data[name_cols[3]].between(tri_75, tri_max), 'tri_sc' + numstr] = 1
    # glucose    
    glu_75 = data[name_cols[4]].quantile(.75)
    glu_max = data[name_cols[4]].max()
    data['glu_sc' + numstr] = 0
    data.loc[data[name_cols[4]].between(glu_75, glu_max), 'glu_sc' + numstr] = 1
    data.drop(data[name_cols[1:]], axis=1, inplace = True)

metab1_cols0 = ['SWANID', 'CHOLRES0', 'HDLRESU0', 'TRIGRES0', 'GLUCRES0']
metab1_cols3 = ['SWANID', 'CHOLRES3', 'HDLRESU3', 'TRIGRES3', 'GLUCRES3']

baseline_metab1 = baseline[metab1_cols0]
visit03_metab1 = visit03[metab1_cols3]

metab1(baseline_metab1, metab1_cols0, '0')
metab1(visit03_metab1, metab1_cols3, '3')

#############################################################
#                                                           #
#                  Metabolic Measures 2                     #
# Includes: BMI, waist to hip ratio                         #
#                                                           #
#############################################################

def metab2(data, name_cols, numstr):
    data.replace(' ', np.nan, inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    # bmi
    bmi_75 = data[name_cols[1]].quantile(.75)
    bmi_max = data[name_cols[1]].max()
    data['bmi_sc' + numstr] = 0
    data.loc[data[name_cols[1]].between(bmi_75, bmi_max), 'bmi_sc' + numstr] = 1
    # waist to hip
    data['whratio' + numstr] = data[name_cols[2]] / data[name_cols[3]]
    whr_75 = data['whratio' + numstr].quantile(.75)
    whr_max = data['whratio' + numstr].max()
    data['whr_sc' + numstr] = 0
    data.loc[data['whratio' + numstr].between(whr_75, whr_max), 'whr_sc' + numstr] = 1

metab2_cols0 = ['SWANID', 'BMI0', 'WAIST0', 'HIP0']
metab2_cols3 = ['SWANID', 'BMI3', 'WAIST3', 'HIP3']

baseline_metab2 = baseline[metab2_cols0]
visit03_metab2 = visit03[metab2_cols3]

#############################################################
#                                                           #
#                  Inflammatory/Neuro                       #
#                                                           #
#############################################################

def inflno(data, name_cols, numstr):
    data.replace(' ', np.nan, inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    # crp
    crp_75 = data[name_cols[1]].quantile(.75)
    crp_max = data[name_cols[1]].max()
    data['crp_sc' + numstr] = 0
    data.loc[data[name_cols[1]].between(crp_75, crp_max), 'crp_sc' + numstr] = 1
    # fib
    fib_75 = data[name_cols[2]].quantile(.75)
    fib_max = data[name_cols[2]].max()
    data['fib_sc' + numstr] = 0
    data.loc[data[name_cols[2]].between(fib_75, fib_max), 'fib_sc' + numstr] = 1
    # dhas
    dhas_25 = data[name_cols[3]].quantile(.25)
    dhas_min = data[name_cols[3]].min()
    data['dhas_sc' + numstr] = 0
    data.loc[data[name_cols[3]].between(dhas_min, dhas_25), 'dhas_sc' + numstr] = 1

inflno_cols0 = ['SWANID', 'CRPRESU0', 'FIBRESU0', 'DHAS0']
inflno_cols3 = ['SWANID', 'CRPRESU3', 'FIBRESU3', 'DHAS3']

baseline_inflno = baseline[inflno_cols0]
visit03_inflno = visit03[inflno_cols3]

#############################################################
#                                                           #
#          Education, Race, Marital Status                  #
#                                                           #
#############################################################

demo = cross[['SWANID', 'ETHNIC', 'DEGREE', 'MARITALGP']]
demo.replace(' ', np.nan, inplace=True)

#############################################################
#                                                           #
#                         Income                            #
#                                                           #
#############################################################

income = baseline[['SWANID', 'INCOME0']]
income.replace(' ', np.nan, inplace=True)
income.replace('-7', np.nan, inplace=True)
income.replace('-8', np.nan, inplace=True)
income.replace('-9', np.nan, inplace=True)

#############################################################
#                                                           #
#                           Age                             #
#                                                           #
#############################################################

baseline_age = baseline[['SWANID', 'AGE0']]
visit03_age = visit03[['SWANID', 'AGE3']]

baseline_age.replace(' ', np.nan, inplace=True)
visit03_age.replace(' ', np.nan, inplace=True)

#############################################################
#                                                           #
#                  Menopause Status                         #
#                                                           #
#############################################################

baseline_meno = baseline[['SWANID', 'STATUS0']]
visit03_meno = visit03[['SWANID', 'STATUS3']]

baseline_meno.replace(' ', np.nan, inplace=True)
visit03_meno.replace(' ', np.nan, inplace=True)


#############################################################
#                                                           #
#               Putting together Baseline AL                #
#                                                           #
#############################################################


