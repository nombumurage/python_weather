import numpy as np
import pandas as pd

filename = "weather.dat"

# with open(filename) as fn:
#     content = fn.readlines()

datContent = [i.strip().split() for i in open("weather.dat").readlines()]
df = pd.DataFrame(datContent=int())

# Calulate the difference between temperatures
# df['diff'] = int(df.ix[:,1]) - int(df.ix[:,2])


# np.diff(axis=1)

print(df.ix[:,1:2])
