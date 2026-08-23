import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr[1, 1:4]) # prints [7 8 9]

print(arr[0:2, 2]) # prints [3 8]

print(arr[0:2, 1:4]) # prints 3-d array 