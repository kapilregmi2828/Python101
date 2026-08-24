# 1-D to 2-D array
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)
newarr = arr.reshape(4,3) #reshape changed the dimension of an array. 2D array 
print(newarr)

newarr2 = arr.reshape(2, 3, 2) # 3D array
print(newarr2)

arr3 = np.array([1,2,3,4,5,6,7,8])
newarr3 = arr3.reshape(2,2,-1) #-1 reshapes the array that you dont know the dimension of. 
print(newarr3)

# flattening the array

arr4 = np.array([[1,2,3],[4,5,6]])
newarr4 = arr4.reshape(-1)
print(newarr4)