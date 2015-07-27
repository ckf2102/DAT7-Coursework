
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

visit03 = pd.read_table('03_Visit3.tsv', low_memory=False)


#############################################################
#                                                           #
#                   Discrimination                          #
#                                                           #
#############################################################

disc_cols0 = ['SWANID', 'COURTES0', 'RESPECT0', 'POORSER0', 'NOTSMAR0', 'AFRAIDO0', 'DISHONS0', 'BETTER0', 'INSULTE0', 'HARASSE0', 'IGNORED0']
disc_cols3 = ['SWANID', 'COURTES3', 'RESPECT3', 'POORSER3', 'NOTSMAR3', 'AFRAIDO3', 'DISHONS3', 'BETTER3', 'INSULTE3', 'HARASSE3', 'IGNORED3']

baseline_disc = baseline[disc_cols0]
visit03_disc = visit03[disc_cols3]

# replacing null values 

baseline_disc.replace(' ',np.nan,inplace=True)
baseline_disc.replace('-9', np.nan,inplace=True)

visit03_disc.replace(' ',np.nan,inplace=True)
visit03_disc.replace('-9', np.nan,inplace=True)

# changing type to float and calculating discrimination average

baseline_disc[disc_cols0[1:]] = baseline_disc[disc_cols0[1:]].astype(float)
baseline_disc['disc0'] = baseline_disc[disc_cols0[1:]].mean(axis=1)

visit03_disc[disc_cols3[1:]] = visit03_disc[disc_cols3[1:]].astype(float)
visit03_disc['disc3'] = visit03_disc[disc_cols3[1:]].mean(axis=1)

# Merging on SWANID 
discrimination = pd.merge(baseline_disc, visit03_disc)

## NOTE:    although the shape of visit03_disc = (2710, 12), the 
##          shape of discrimination = (2478, 45). Not only is there
##          loss to follow-up, but participants who may have skipped
##          visit01 could be re-evaluated for visit03
##          I could use an outer join, to capture all participants, even
##          those lost to follow-up if I wanted to


# dropping extraneous columns 

discrimination.drop(discrimination[disc_cols0[1:]], axis=1, inplace = True)
discrimination.drop(discrimination[disc_cols3[1:]], axis=1, inplace = True)

# boxplot all of the discrimination scores

discrimination.drop('SWANID', axis=1).plot(kind='box')

discrimination.disc0.describe()
discrimination.disc3.describe()

#############################################################
#                                                           #
#                   Perceived Stress                        #
#                                                           #
#############################################################

pstress_cols3 =['SWANID', 'CONTROL3', 'YOURWAY3', 'PILING3', 'ABILITY3']

cross_pstress = cross[['SWANID', 'P_STRESS']]
cross_pstress.rename(columns={'P_STRESS':'pstress0'}, inplace=True)

visit03_pstress = visit03[pstress_cols3]

# replacing null values

cross_pstress.replace(' ',np.nan,inplace=True)
visit03_pstress.replace(' ',np.nan,inplace=True)

visit03_pstress.replace('-1',np.nan,inplace=True)

# changing type to float

cross_pstress['pstress0'] = cross_pstress['pstress0'].astype(float)
visit03_pstress[pstress_cols3[1:]] = visit03_pstress[pstress_cols3[1:]].astype(float)

# calculating pstress values

visit03_pstress['pstress3'] = visit03_pstress[pstress_cols3[1:]].sum(axis=1)


# Merging on SWANID 

pstress = pd.merge(cross_pstress, visit03_pstress)

# dropping extraneous columns 

pstress.drop(pstress[pstress_cols3[1:]], axis=1, inplace = True)

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
    data.dropna(inplace=True)

sysbp_cols0 = ['SWANID', 'SYSBP10', 'SYSBP20', 'SYSBP30']
sysbp_cols3 = ['SWANID', 'SYSBP13', 'SYSBP23']

baseline_sysbp = baseline[sysbp_cols0]
visit03_sysbp = visit03[sysbp_cols3]

sysbpcalc(baseline_sysbp, sysbp_cols0, 'sysbp_mean0', 'sysbp_sc0')
sysbpcalc(visit03_sysbp, sysbp_cols3, 'sysbp_mean3', 'sysbp_sc3')

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
    data.dropna(inplace=True)

diabp_cols0 = ['SWANID', 'DIABP10', 'DIABP20', 'DIABP30']
diabp_cols3 = ['SWANID', 'DIABP13', 'DIABP23']

baseline_diabp = baseline[diabp_cols0]
visit03_diabp = visit03[diabp_cols3]

diabpcalc(baseline_diabp, diabp_cols0, 'diabp_mean0', 'diabp_sc0')
diabpcalc(visit03_diabp, diabp_cols3, 'diabp_mean3', 'diabp_sc3')

#############################################################
#                                                           #
#                  Metabolic Measures 1                     #
# Includes: cholesterol, HDL, triglycerides, and glucose    #
#                                                           #
#############################################################

def metab1(data, name_cols, numstr):
    data.replace(' ', np.nan, inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    data.dropna(inplace=True)
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
    #data.drop(data[name_cols[1:]], axis=1, inplace = True)

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
    data.dropna(inplace=True)
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

metab2(baseline_metab2, metab2_cols0, '0')
metab2(visit03_metab2, metab2_cols3, '3')

#############################################################
#                                                           #
#                  Inflammatory/Neuro                       #
#                                                           #
#############################################################

def inflno(data, name_cols, numstr):
    data.replace(' ', np.nan, inplace=True)
    data[name_cols[1:]] = data[name_cols[1:]].astype(float)
    data.dropna(inplace=True)
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

inflno(baseline_inflno, inflno_cols0, '0')
inflno(visit03_inflno, inflno_cols3, '3')

#############################################################
#                                                           #
#          Education, Race, Marital Status                  #
#                                                           #
#############################################################

demo = cross[['SWANID', 'ETHNIC', 'DEGREE', 'MARITALGP']]
demo.replace(' ', np.nan, inplace=True)

demo['ETHNIC'] = demo.ETHNIC.map({'1':'AfAm', '8':'0Asian', '9':'0Asian', '10':'White', '13':'Hispanic'})
demo['DEGREE'] = demo.DEGREE.map({'1':1, '2':2, '3':3, '4':4, '5':5})
demo['MARITALGP'] = demo.MARITALGP.map({'1':0, '2':1, '3':0, '4':0})

ethnic_dummies = pd.get_dummies(demo.ETHNIC, prefix='Race').iloc[:, 1:]
demo = pd.concat([demo, ethnic_dummies], axis=1)

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

income['INCOME0'] = income.INCOME0.map({'1':'Low', '2':'M1', '3':'M2', '4':'High'})

income_dummies = pd.get_dummies(income.INCOME0, prefix = 'Income').iloc[:, 1:]
income = pd.concat([income, income_dummies], axis=1)

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

visit03_meno['STATUS3'] = visit03_meno.STATUS3.map({'1':3, '2':3, '3':2, '4':2, '5':1, '6':1, '7':0})
# 3 = post
# 2 = peri
# 1 = pre
# 0 = hormone therapy usse

#############################################################
#                                                           #
#               Putting together Baseline AL                #
#                                                           #
#############################################################

baseline_response = pd.merge(baseline_sysbp, baseline_diabp)
baseline_response = pd.merge(baseline_response, baseline_metab1)
baseline_response = pd.merge(baseline_response, baseline_metab2)
baseline_response = pd.merge(baseline_response, baseline_inflno)

score_cols0 = ['sysbp_sc0', 'diabp_sc0', 'cholest_sc0', 'hdl_sc0', 'tri_sc0', 'glu_sc0', 'bmi_sc0', 'whr_sc0', 'crp_sc0', 'fib_sc0', 'dhas_sc0']
baseline_response['allo0'] = baseline_response[score_cols0].sum(axis=1)

baseline_response = baseline_response[['SWANID', 'allo0']]

#############################################################
#                                                           #
#               Putting together Visit 03 AL                #
#                                                           #
#############################################################

visit03_response = pd.merge(visit03_sysbp, visit03_diabp)
visit03_response = pd.merge(visit03_response, visit03_metab1)
visit03_response = pd.merge(visit03_response, visit03_metab2)
visit03_response = pd.merge(visit03_response, visit03_inflno)

score_cols3 = ['sysbp_sc3', 'diabp_sc3', 'cholest_sc3', 'hdl_sc3', 'tri_sc3', 'glu_sc3', 'bmi_sc3', 'whr_sc3', 'crp_sc3', 'fib_sc3', 'dhas_sc3']
visit03_response['allo3'] = visit03_response[score_cols3].sum(axis=1)

visit03_response = visit03_response[['SWANID', 'allo3']]

data_response = pd.merge(baseline_response, visit03_response)

#############################################################
#                                                           #
#               Putting together Features                   #
#                                                           #
#############################################################

data_features = pd.merge(discrimination, pstress)
data_features = pd.merge(data_features, baseline_host)
data_features = pd.merge(data_features, demo)
data_features = pd.merge(data_features, income)
data_features = pd.merge(data_features, baseline_age)
data_features = pd.merge(data_features, baseline_meno)
data_features = pd.merge(data_features, visit03_age)
data_features = pd.merge(data_features, visit03_meno)

#############################################################
#                                                           #
#       Putting together all data, some analysis            #
#                                                           #
#############################################################

import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from scipy import stats as scs

data = pd.merge(data_features, data_response)
data.groupby('ETHNIC').allo0.describe()

float_cols = ['AGE0', 'AGE3']
data[float_cols] = data[float_cols].astype(float)

data[['ETHNIC','DEGREE']].corr()
data[['allo0', 'allo3']].plot(kind='box')

# drinks.beer.hist(by=drinks.continent, sharex=True, sharey=True)
# drinks.plot(kind='scatter', x='beer', y='wine', alpha=0.3)
# drinks.continent.value_counts().plot(kind='bar')

data.INCOME0.value_counts(sort=False).plot(kind='bar')

data.boxplot(column='allo3', by='STATUS3')

race_income_obs = np.array([[42, 281, 355, 159], [89, 159, 136, 22], [13, 99, 143, 74], [39, 30, 6, 2]]).T
scs.chisquare(race_income_obs, axis=None)