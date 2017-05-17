# Variable that holds the external data file
filename = "weather.dat"

# Code to open and read the .dat file
with open(filename) as text_file:
     lines = text_file.read().splitlines()

# Initialize empty array to store the result
diff = []

for i in range(2,len(lines)):
    removedSpaces = lines[i].strip()
    eachcolumn = removedSpaces.split()

    try:
        # For values without the asteric
        if ("*" not in eachcolumn[1] and "*" not in eachcolumn[2]):
            difference = int(eachcolumn[1]) - int(eachcolumn[2])
            diff.append(eachcolumn[0]+ " " +str(difference))

        # Values with asteric for column MxT.  This is supposed to remove the asteric
        elif (eachcolumn[1].endswith("*")):
            eachcolumn[1] = eachcolumn[1][:-1]
            difference = int(eachcolumn[1]) - int(eachcolumn[2])
            diff.append(eachcolumn[0]+ " " +str(difference))

        # Values with asteric for column MnT.  This is supposed to remove the asteric
        elif (eachcolumn[2].endswith("*")):
            eachcolumn[2]= eachcolumn[2][:-1]
            difference = int(eachcolumn[1]) - int(eachcolumn[2])
            diff.append(eachcolumn[0]+ " " +str(difference))

    # This deals with the float values at the very end of the dataset
    except ValueError:
        difference = float(eachcolumn[1]) - float(eachcolumn[2])
        diff.append(difference)
        
# Prints out the highest temperature spread
print max(diff)
