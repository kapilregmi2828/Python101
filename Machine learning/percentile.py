# Percentile is how you compare with other people. 
# It is a measure of how many people scored below you. 
# For example, if you are in the 90th percentile, that means you scored better than 90% of the people who took the test.

import numpy as np
speed = [97,90,88,83,87,111,100,103,87,94]
x = np.percentile(speed, 90)
print(x)        

age = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = np.percentile(age, 75)
print(y)            