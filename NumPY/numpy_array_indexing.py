import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.ndim)

print(arr[1,1]) # accessing 2nd element of 2nd array

a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[8,5,4]]])
print(a)
print(a.ndim)
print(a[1,0,1]) # accessing 2nd element of 2nd array of 1st array

print(a[0,1,1] + a[1,1,1]) # prints 10

