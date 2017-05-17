#Solution
Pseudo code
1. Step one would be to read the data from the external file ('weather.dat')
2. Load the data from the .dat file as lists of lists.
3. Initialize an empty array which will be used to output the final result
3. Clean the data to remove spaces.
4. Identify each column as arrays.
5. Loop through each data element in each column and subtract it from the other column.
6. Add the resulting difference to the array.
7. While appending the result add the corresponding day value from the first column (Dy).
8. Get the highest temperature spread using max() method and print it.

#Assumptions
The script runs true for the specific dataset. Any changes in the dataset might affect the functioning of the script

#To Run the Program
1. Ensure python is installed on the machine. Version used for this script is 2.7.12
2. Run : python weather.py
