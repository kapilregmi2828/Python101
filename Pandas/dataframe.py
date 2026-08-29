# DataFrame is a 2-D array or a table with rows and columns. 

import pandas as pd

data = {
    "calories": [450, 390, 380],
    "duration": [50, 40, 30]
}

df = pd.DataFrame(data)
print(df)

#loc attribute returns one or more specifies rows. 
print("________________________________")

print(df.loc[0])

print("________________________________")

print(df.loc[[0,1,2]])