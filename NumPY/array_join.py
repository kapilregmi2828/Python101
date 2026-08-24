# concatenate() is to join 2 arrays into a single array

# stack() is same as concatenate but its done along a new axis.

# hstack() is to stack along rows

# vstack() is to stack along columns

# dstack() is to stack along height or depth 
import numpy as np

arr1 = np.array([1,2,3,4])

arr2 = np.array([5,6,7,8])

arr = np.concatenate((arr1, arr2))

print(arr)
print("---------------------------")
arr_h = np.hstack((arr1, arr2))
print(arr_h)

print("---------------------------")

arr_v = np.vstack((arr1, arr2))
print(arr_v)

print("---------------------------")

arr_d = np.dstack((arr1, arr2))
print(arr_d)

