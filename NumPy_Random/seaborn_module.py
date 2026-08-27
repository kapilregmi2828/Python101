# seaborn module is a library that uses Matplotlib to plot graphs. It is used to visualize random distributions.

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0,1,2,3,4,5])
plt.show() # shows a histogram

sns.displot([0,1,2,3,4,5], kind = "kde")
plt.show()