import pandas as pd
import numpy as np

#Assumes the file has a fixed width delimiter or rather the type of delimiter is unknown
df = pd.read_fwf('weather.dat',header = 0, index_col = None)

####Cleaning the data#####
#Drop rows with NaN values
df = df.dropna(axis = 0, how = 'all')
#Drop any columns with NaN values, (change 'any' to 'all' to drop all columns with all NaN)
df = df.dropna(axis = 1, how = 'any')
print ('Below is the first overview of the data.')
print (df)

#removing * manually since.
# Learn how to remove * automatically with dataframe
df.iloc[25,1]= 97
df.iloc[8,2] = 32

diff= np.float_(df['MxT'])- np.float_(df['MnT'])

print diff
print max(diff)
