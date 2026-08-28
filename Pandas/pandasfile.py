# Pandas is a Python Library used for working with data sets.
# Its function is to analyzing, cleaning, exploring, and manipulating data.

# Pandas can clean messy data sets and make them readable and relevant. 
# Its like presenting data into table. 

import pandas as pd
a = [1,7,2]

# Pandas Series is like a column in a table. It is a 1-D array holding data of any type.
myvar = pd.Series(a)
print(myvar)

b = [2,4,6]
myvar2 = pd.Series(b, index = ["x", "y", "z"])
print(myvar2)

print(myvar2["z"])