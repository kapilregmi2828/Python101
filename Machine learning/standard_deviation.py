# Standard Deviation is a number that describes how spread out the values in a data set are from the mean.
# A low standard deviation indicates that the values tend to be close to the mean, 
# while a high standard deviation indicates that the values are spread out over a wider range.

import numpy as np
speed = [97,90,88,83,87,111,100,103,87,94]
# Standard Deviation
x = np.std(speed)
print(x)  

# variance is just the square of the standard deviation. 
# It is a measure of how far a set of numbers are spread out from their average value.

y = np.var(speed)
print(y)    