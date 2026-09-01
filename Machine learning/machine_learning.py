# Machine Learning is a way of teaching computers to find patterns in data / examples 
# so they can make predictions or decisions without being explicitly programmed to do so. 
# It is a subset of artificial intelligence (AI) that focuses on the development of algorithms and 
#  statistical models that enable computers to learn from and make predictions based on data.

# Mean
import numpy as np
from scipy import stats

speed = [97,90,88,83,87,111,100,103,87,94]
x = np.mean(speed)
print(x)

# Median
y = np.median(speed)
print(y)

# Mode
z = stats.mode(speed)
print(z)    