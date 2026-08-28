# We can set key- value objects in pandas. Here Keys will act as index of the elements.

import pandas as pd

calories = { "day1": 400, "day2": 380, "day3": 450}

myvar = pd.Series(calories)
print(myvar)

myvar2 = pd.Series(calories, index =["day1", "day3"])
print(myvar2)