# shape attribute returns a tuple with the dimension of the array. (rows, columns)

import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])

print(arr.shape) #(2,4)

arr2 = np.array([1,2,3,4], ndmin=5)

print(arr2)
print(arr2.shape)