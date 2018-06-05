#!/usr/bin/python
import os
import pyarrow.parquet as pq
import seaborn as sns

#This script requires 'dataExploration.py' to run before to unzip our data
folder = '/data/'
filename = 'TopVideoSmall'

## Load data as pandas dataframe using pyArrow
dS = pq.ParquetDataset(os.getcwd() + folder + filename)
df = dS.read().to_pandas()

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

## We have mixed types in our dataset
## Select only numberic columns
dfNumeric = df.select_dtypes(exclude=['object', 'long', 'datetime64'])
dfString =  df.select_dtypes(include=['object'])

# Quiz:
#
# How many observations are in our dataframe?
# How many Numeric features do we have?
# How many are categorical?
# How many related to dates? (types: long, datetime64)
#####

print len(df)
print len(dfNumeric.columns)
print len(dfString.columns)
dfString.columns
#####


#### Histrograms

## Lets look at the distribution of CTR, Click and View counts
##  for one of the tiles e.g. 'radar large'
tilesChart = 'precip start large'
for metric, bins in zip(['_r', '_vi', '_cl'], [50,25,25]):
    df[(df[tilesChart + metric] >0) & (df[tilesChart + metric] < 100)].hist(tilesChart + metric, bins = bins)

## Comparing the CTR distribution of two  tiles
bins = 25 # How many bins should there be in the histogram
tilesChart = [x + "_r" for x in ['radar large','radar small']] # List of columns to be charted
df[tilesChart][~(df[tilesChart] < 0).any(axis=1) & ~(df[tilesChart] > 100).any(axis=1)].plot.hist(bins = bins, alpha=0.5)

#### Scatter plots

## Look out: Scatter plots can break your Script,
## as there can be millions of dots. Downsample!
tilesChart = [x + "_r" for x in ['radar large',
                                 'precip start large']] # List of columns to be charted
dfSampled = df[tilesChart][~(df[tilesChart] < 0).any(axis=1) &
                           ~(df[tilesChart] > 100).any(axis=1)].sample(frac = 0.05) #Sampling 1% of observations
sns.lmplot(x=tilesChart[0],
           y=tilesChart[1],
           data=dfSampled,
           fit_reg=True) # Seaborn Plot with regression line


# Quiz:
#
# Plot scatter plots between two other tiles and share with us
# Copy relevant code first and then adapt it below
#####


#####