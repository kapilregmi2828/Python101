# to read a csv (comma separaated values) 

import pandas as pd

df = pd.read_csv('data.csv')

#print(df)

# to_string() prints the whole table. 
print(df.to_string())

# if you hace large data with many rows, pandas will only return first and last 5 rows. 