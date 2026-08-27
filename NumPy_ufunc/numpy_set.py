# set is a collection of unique elements.

import numpy as np

arr = np.array([1,1,2,3,4,5,5,6,7])
x = np.unique(arr)
print(x)

# union1d() 

arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])

newarr1 = np.union1d(arr1, arr2)
print(newarr1)

# intersect1d()

newarr2 = np.intersect1d(arr1,arr2)
print(newarr2)

#setdiff1d()

newarr3 = np.setdiff1d(arr1, arr2, assume_unique=True)
print(newarr3)

#setxor1d()

newarr4 = np.setxor1d(arr1,arr2, assume_unique=True)
print(newarr4)