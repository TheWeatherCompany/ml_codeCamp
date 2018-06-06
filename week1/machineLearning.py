#!/usr/bin/python
import os
import pyarrow.parquet as pq
## sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

## Pre-requesites:
## This script requires 'dataExploration.py' to run before to unzip our data
folder = '/data/'
filename = 'TopVideoSmall'

## Load data as pandas dataframe using pyArrow
dS = pq.ParquetDataset(os.getcwd() + folder + filename)
df = (dS.read()
      .to_pandas()
      .select_dtypes(exclude=['object', 'long', 'datetime64'])
      .drop_duplicates()
      .reset_index()
      )

### Data Preparation
## Renaming column names for tile related metrics
allTiles = [
    'radar large'
    ,'radar small'
    ,'precip start large'
    ,'precip end large'
    ,'precip start small'
    ,'precip end small'
    ,'tomorrow\'s forecast large'
    ,'weekend forecast large'
    ,'daily forecast large'
    ,'hourly forecast large'
    ,'breaking news video small'
    ,'breaking news video large'
    ,'lightning small'
    ,'t-storm now small'
    ,'winter storm now small'
    ,'snow accumulation small'
    ,'winter storm forecast small'
    ,'t-storm soon small'
    ,'precip intensity'
    ,'cold and flu small'
    ,'gorun small'
    ,'feels like small'
    ,'boat and beach small'
    ,'tomorrow\'s forecast small'
    ,'weekend forecast small'
    ,'sunset\/sunrise small'
    ,'hourly forecast small'
    ,'daily forecast small'
    ,'top video small'
    ,'top video large'
    ,'severe alerts table'
    ,'editorial calendar large'
    ,'alert small'
    ,'alert large'
    ,'road conditions small'
    ,'radar extra large'
    ,'video extra large'
]
tileColumns = [x for x in df.columns if 'streams_ML_d28_t' in x]
for metric in ['_r', '_vi', '_cl']:
    df.rename(columns =
    dict(
        zip(
         ['context_streams_ML_d28_t_t' + str(x) + metric for x in range(1,len(allTiles))],
         [x + metric for x in allTiles]
        )
    ), inplace = True)

X = df[[x for x in df.columns        # Features
        if x != 'label']].fillna(0)  #We can't train a model with empty cells in our datafram
Y = df['label'].values.astype(int)   # Label
# Split Data and Train Model
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=100)

# Define Classifier
rfc = RandomForestClassifier(criterion="gini",
                             random_state=100,
                             max_depth=10,
                             n_estimators=10,  # Number of Trees
                             min_samples_leaf=8,  # Percentage of Sample Size
                             min_samples_split=20)

rfc.fit(X_train, y_train)

# Model Metrics
y_pred = rfc.predict(X_test)
print " Accuracy is ", accuracy_score(y_test, y_pred) * 100
print " Confusion Matrix:", confusion_matrix(y_test, y_pred)


##Print Feature Importance
## Filters out features with low importance
featureNames = df[[x for x in df.columns if x != 'label']].columns
j = 0
fi =  rfc.feature_importances_
for i in featureNames:
    if fi[j] >= fi.mean():
        print i, fi[j]
    j += 1