#!/usr/bin/python
import os
import pyarrow.parquet as pq
import sklearn
#This script requires 'dataExploration.py' to run before to unzip our data
folder = '/data/'
filename = 'TopVideoSmall'

## Load data as pandas dataframe using pyArrow
dS = pq.ParquetDataset(os.getcwd() + folder + filename)
df = dS.read().to_pandas()

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
    df.rename(columns = dict(zip([y for y in tileColumns if metric in y], [x + metric for x in allTiles])), inplace = True)

