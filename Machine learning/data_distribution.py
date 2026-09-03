# create an array containing 250 random floats between 0 and 5

import numpy as np
import matplotlib.pyplot as plt
arr = np.random.uniform(0,5,250)
#print(arr)

plt.hist(arr, 5)
plt.show()
