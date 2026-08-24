#ndenumerate() iterates through each element of array and returns the corresponding index as well

import numpy as np

arr = np.array([1,2,3])

for idx, x in np.ndenumerate(arr):
    print(idx, x)

arr2 = np.array([[1,2,3],[4,5,6]])

for idx,x in np.ndenumerate(arr2):
    print(idx,x)