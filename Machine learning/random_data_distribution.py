import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(5,1,1000) # mean=5, std_dev=1, size=1000
y = np.random.normal(10,2,1000) # mean=10, std_dev=2, size=1000
plt.scatter(x, y)
plt.show()