import numpy as np
import pandas as pd

filename = "weather.dat"

with open(filename) as fn:
    content = fn.readlines()

df = pd.DataFrame(content)

#Calulate the difference between temperatures
# df['diff'] = df['MxT']- df['Mnt']


np.diff(df.values, axis=1)

print(df['MxT'])
