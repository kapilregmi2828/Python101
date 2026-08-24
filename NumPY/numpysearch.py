import numpy as np

arr = np.array([1,2,3,4,5,4,4])

x = np.where(arr == 4)
print(x) # prints indexes of 4

arr2 = np.array([10,14,93,41,8,7])

x = np.where(arr2 % 2 == 1)
print(x)

arr3 = np.array([1,3,5,7])
x = np.searchsorted(arr3,[2,4,6])
print(x) # print the indexes of 2 4 6 such that arr3 will remain sorted.
