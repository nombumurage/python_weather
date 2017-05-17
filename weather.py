# import numpy as np
# import pandas as pd

# read weather.dat to a list of lists
# datContent = [i.strip().split() for i in open("weather.dat").readlines()]
# df = pd.DataFrame(datContent)
#
# column1 = df.ix [:, 1]
# for i in column1:
#
# print(intColumn1)

# Calulate the difference between the highest temperature points(*)
# print(df.ix[[27],1])
# print(df.ix[[10],2])

filename = "weather.dat"

with open(filename) as text_file:
     lines = text_file.read().splitlines()
diff = []

for i in range(2,len(lines)):
    removedSpaces = lines[i].strip()
    eachcol = removedSpaces.split()

    try:
        if ("*" not in eachcol[1] and "*" not in eachcol[2]):
            difference = int(eachcol[1]) - int(eachcol[2])
            diff.append(difference)
        else:
            eachcol[1]= eachcol[1][:-1]
            eachcol[2] = eachcol[2][:-1]
            difference = int(eachcol[1]) - int(eachcol[2])
            diff.append(difference)

    except ValueError:
        difference = float(eachcol[1]) - float(eachcol[2])
        diff.append(difference)

print diff
print max(diff)
