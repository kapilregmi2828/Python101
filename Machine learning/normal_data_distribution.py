# Normal Data Distribution as know as Gaussian Distribution forms Bell Curve.
#  It is a continuous probability distribution that is symmetrical around its mean, w
# ith the majority of the data points falling close to the mean and 
# fewer data points appearing as you move further away from the mean. 
# The shape of the curve is determined by two parameters: the mean (μ) and the standard deviation (σ). 
# The mean determines the center of the distribution, while the standard deviation determines the spread or width of the curve. 
# A smaller standard deviation results in a narrower curve, while a larger standard deviation results in a wider curve.

import numpy as np
import matplotlib.pyplot as plt
arr = np.random.normal(5, 2, 100000)  # mean=5, std_dev=2, size=1000
plt.hist(arr, 100)
plt.show()