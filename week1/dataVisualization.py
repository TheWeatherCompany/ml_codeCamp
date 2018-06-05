#!/usr/bin/python
import os
import pyarrow.parquet as pq

#This script requires 'dataExploration.py' to run before to unzip our data
folder = '/data/'
filename = 'TopVideoSmall'

## Load data as pandas dataframe using pyArrow
dS = pq.ParquetDataset(os.getcwd() + folder + filename)
df = dS.read().to_pandas()

## We have mixed types in our dataset
## Select only numberic columns
dfNumeric = df.select_dtypes(exclude=['object', 'long', 'datetime64'])
dfString =  df.select_dtypes(include=['object'])

# Quiz:
#
# How many Numeric features do we have?
# How many are categorical?
# How many related to dates? (types: long, datetime64)
#####


#####

## Print the Column Names by Type
# print dfNumeric.dtypes, dfString.dtypes

## Create a list of columns containing substring
## these are all the CTR, view and click statistics by tile
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
print allTiles, tileColumns

## Lets look at the distribution for one of the tiles e.g. 'radar large'
oneTile = 'radar large'
tileColumn = 'context_streams_ML_d28_t_t' + str(allTiles.index(oneTile) + 1)
for metric, bins in zip(['r', 'cl', 'vi'], [100,25,25]):
    df[df[tileColumn + '_' + metric] < 100].hist(tileColumn + '_' + metric, bins = bins)

## How are two tiles correlated to each other

xName = 'radar large'
yName = 'precip start large'
xColumn = 'context_streams_ML_d28_t_t' + str(allTiles.index(xName) + 1) + '_r'
yColumn = 'context_streams_ML_d28_t_t' + str(allTiles.index(yName) + 1) + '_r'

## Scatter plots can break your Script. Downsample!
dfSmall = df.sample(frac = 0.01)
# Simple Scatter plot
dfSmall.plot.scatter(x = xColumn, y = yColumn)


# Plot with regression line
import seaborn as sns
sns.lmplot(x=xColumn,y=yColumn,data=dfSmall,fit_reg=True)


# Quiz:
#
# Plot scatter plots between two other tiles and share with us
# Copy relevant code first and then adapt it
#####


#####