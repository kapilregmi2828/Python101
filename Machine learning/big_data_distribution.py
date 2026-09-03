import numpy as np
import matplotlib.pyplot as plt
arr = np.random.uniform(0,5,100000)
plt.hist(arr, 100)
plt.show()