#!/usr/bin/python
import pickle
import pandas as pd
import zipfile
import pyarrow.parquet as pq

#Unzip data
folder = 'data/'
filename = 'TopVideoSmall'
zip_ref = zipfile.ZipFile(folder + filename + '.zip', 'r')
zip_ref.extractall(folder)
zip_ref.close()

#Load data as pandas dataframe
dS = pq.ParquetDataset(folder + filename)
df = dS.read().to_pandas()

print df.dtypes
