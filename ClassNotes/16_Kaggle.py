# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:02:21 2015

@author: Corinne
"""

import pandas as pd
test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv', index_col = 0)

closed_train = train[train.OpenStatus == 0]
open_train = train[train.OpenStatus == 1]

closed_train.OwnerUndeletedAnswerCountAtPostTime.value_counts()
open_train.OwnerUndeletedAnswerCountAtPostTime.value_counts()

train.OwnerUndeletedAnswerCountAtPostTime.plot(kind = 'box')

# drinks.boxplot(column='beer', by='continent')

train.boxplot(column='OwnerUndeletedAnswerCountAtPostTime', by='OpenStatus')

train.boxplot(column='ReputationAtPostCreation', by='OpenStatus')

closed_train.ReputationAtPostCreation.value_counts()
open_train.ReputationAtPostCreation.value_counts()

train['timing'] = train.PostCreationDate - train.OwnerCreationDate

# convert a string to the datetime format
#ufo['Time'] = pd.to_datetime(ufo.Time)
#ufo.Time.dt.hour                        # datetime format exposes convenient attributes
#(ufo.Time.max() - ufo.Time.min()).days  # also allows you to do datetime "math"

train['PostCreationTime'] = pd.to_datetime(train.PostCreationDate)
train['OwnerCreationTime'] = pd.to_datetime(train.OwnerCreationDate)

train['TimeDif'] = train.PostCreationTime - train.OwnerCreationTime

"""
Feature Exploration - Query Number
"""

train.OpenStatus.value_counts()

# testing the hypothesis that userid could pop up multiple times in the code
train.OwnerUserId.value_counts()

# let's look at the user with the most queries
train[train.OwnerUserId == 466534].describe()
train[train.OwnerUserId == 466534].head()

# let's look at another user with a lot of queries
train[train.OwnerUserId == 39677].describe()
train[train.OwnerUserId == 39677].head()

"""
Feature Exploration - Reputation Status
"""

train.groupby('OpenStatus').ReputationAtPostCreation.describe()
    # it looks like, at a very aggregate level, that those with higher
    # reputation have more open questions

# filter the data to create a better histogram
train[train.ReputationAtPostCreation < 1000].ReputationAtPostCreation.hist(by=train.OpenStatus, sharex = True, sharey = True)
    # it looks like reputation for closed questions are much lower
    # reputation for open questions is distributed more (slightly) to the right

"""
Feature Exploration - Answer Count
"""

train.rename(columns={'OwnerUndeletedAnswerCountAtPostTime':'Answers'}, inplace = True)

train.groupby('OpenStatus').Answers.describe()
    # again, our distribution is slightly higher (in general) for those people who have open questions

train[train.Answers < 100].Answers.hist(by=train.OpenStatus, sharex = True, sharey = True)

"""
Creating our first submission
"""

# sometimes you'll be doing a lot of computations on the training set
# that you will need to replicate on the testing set

def make_features(filename):
        df = pd.read_csv(filename, index_col = 0)
        df.rename(columns={'OwnerUndeletedAnswerCountAtPostTime':'Answers'}, inplace = True)
        df['PostCreationTime'] = pd.to_datetime(df.PostCreationDate)
        df['OwnerCreationTime'] = pd.to_datetime(df.OwnerCreationDate)       
        df['TimeDif'] = (df.PostCreationTime - df.OwnerCreationTime).dt.days
        df['BodyLength'] = df.BodyMarkdown.apply(len)
        df['TitleLength'] = df.Title.apply(len)
        df['NumTags'] = df.loc[:, 'Tag1':'Tag5'].notnull().sum(axis=1)
        return df

train = make_features('train.csv')
test = make_features('test.csv')

feature_cols = ['ReputationAtPostCreation', 'Answers']
X = train[feature_cols]
y = train.OpenStatus

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
logreg.fit(X_train, y_train)
logreg.coef_

y_pred_class = logreg.predict(X_test)
y_pred_prob = logreg.predict_proba(X_test)[:, 1]

# now doing evaluations

from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred_class)
print metrics.confusion_matrix(y_test, y_pred_class)
print metrics.roc_auc_score(y_test, y_pred_prob)
print metrics.log_loss(y_test, y_pred_prob)

# log loss: 

# AUC is a reward function: higher is better
# Log Loss: loss function, lower is better
    # it is rewarding you for predicted probabilities that are 
    # close to the actual values (i.e. 80-90% vs 50-60%)
        # log loss punishes when you're really confident and really wrong
    # log loss for the null model will be 0.693

# cross validation score
from sklearn.cross_validation import cross_val_score
cross_val_score(logreg, X, y, cv = 10, scoring='log_loss')
cross_val_score(logreg, X, y, cv = 10, scoring='log_loss').mean()

# now retraining model on the entire training data set
logreg.fit(X, y)

X_oos = test[feature_cols]  # oos = out of sample
oos_pred_prob = logreg.predict_proba(X_oos)[:, 1]   # oos predicted prob

# our submission requires ID and predicted probabilities

pd.DataFrame({'id':test.index, 'OpenStatus':oos_pred_prob}).set_index('id').to_csv('sub1.csv')
    # set_index makes the ID the first column

"""
So let's test some new theories!

Longer body or title or tags --> more likely to be open
"""

# body length
# applying a function to a series --> .apply(fx)
train['BodyLength'] = train.BodyMarkdown.apply(len)
train.groupby('OpenStatus').BodyLength.describe()

# what about title length?
train['TitleLength'] = train.Title.apply(len)
train.groupby('OpenStatus').TitleLength.describe()

# now we need to build a feature to count tag length

# baseline_bp['NumBP'] = baseline_bp.isnull().sum(axis=1)

train.Tag1.nunique()
train.groupby('Tag1').OpenStatus.mean()

# loc: access rows and columns by name
# counts of tags! one line of code
train['NumTags'] = train.loc[:, 'Tag1':'Tag5'].notnull().sum(axis=1)

"""
Checking account age
"""

train.TimeDif[train.TimeDif < 0].describe()
train.TimeDif[train.TimeDif > 0].describe()
train.TimeDif.describe()

"""
Now adding more features to our model
"""

feature_cols = ['ReputationAtPostCreation', 'Answers', 'TitleLength', 'BodyLength', 'NumTags', 'TimeDif']
X = train[feature_cols]
cross_val_score(logreg, X, y, cv=10, scoring='log_loss').mean()

# now retraining model on the entire training data set
logreg.fit(X, y)

X_oos = test[feature_cols]  # oos = out of sample
oos_pred_prob = logreg.predict_proba(X_oos)[:, 1]   # oos predicted prob

# our submission requires ID and predicted probabilities
pd.DataFrame({'id':test.index, 'OpenStatus':oos_pred_prob}).set_index('id').to_csv('sub2.csv')
    # set_index makes the ID the first column

"""
What about all the text data??
"""

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(stop_words='english')

dtm = vect.fit_transform(train.Title)

from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

cross_val_score(nb, dtm, train.OpenStatus, cv=10, scoring = 'log_loss').mean()

oos_dtm = vect.transform(test.Title)

nb.fit(dtm, train.OpenStatus)
oos_pred_prob = nb.predict_proba(oos_dtm)[:, 1]

pd.DataFrame({'id':test.index, 'OpenStatus':oos_pred_prob}).set_index('id').to_csv('sub3.csv')

# there is a lot of signal in the title, more than the other features we looked at
# log loss score is significantly better than our cross validation score which tells
    # us that there's something different about test.csv... (date!!)