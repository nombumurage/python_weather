# Variable that holds the external data file
filename = "weather.dat"

# Code to open and read the .dat file
with open(filename) as text_file:
     lines = text_file.read().splitlines()

# Initialize empty array to store the result
diff = []

for i in range(2,len(lines)):
    removedSpaces = lines[i].strip()
    eachcol = removedSpaces.split()

    try:
        # For values without the asteric
        if ("*" not in eachcol[1] and "*" not in eachcol[2]):
            difference = int(eachcol[1]) - int(eachcol[2])
            diff.append(eachcol[0]+ " " +str(difference))

        # Values with asteric for column MxT.  This is supposed to remove the asteric
        if (eachcol[1].endswith("*")):
            eachcol[1] = eachcol[1][:-1]
            difference = int(eachcol[1]) - int(eachcol[2])
            diff.append(eachcol[0]+ " " +str(difference))

        # Values with asteric for column MxT.  This is supposed to remove the asteric
        elif (eachcol[2].endswith("*")):
            eachcol[2]= eachcol[2][:-1]
            difference = int(eachcol[1]) - int(eachcol[2])
            diff.append(eachcol[0]+ " " +str(difference))

    # This deals with the float values at the very end of the dataset
    except ValueError:
        difference = float(eachcol[1]) - float(eachcol[2])
        diff.append(difference)

print max(diff)
