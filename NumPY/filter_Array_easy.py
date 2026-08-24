import numpy as np

arr = np.array([41,42,43,44])

filter_arr = arr > 42

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


arr2 = np.array([1,2,3,4,5,6,7,8,9])

filter_arr2 = arr2 % 2 == 0

newarr2 = arr2[filter_arr2]
print(filter_arr2)
print(newarr2)