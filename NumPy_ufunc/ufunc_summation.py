# Numpy summations
# sum() function adds all the elements of both array
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])

newarr = np.sum([arr1,arr2])
print(newarr)

# cumsum() function does the cummalitave sum of all the elements. 
x = np.cumsum([arr1,arr2])
print(x)

# Numpy Products

arr3 = np.array([1,2,3,4])
y = np.prod(arr3)
print(y)

# cumprod() does the cummalitave production of all the elements. 

# Numpy difference 

arr4 = np.array([10,15,20,5])
z = np.diff(arr4)
print(z)
c = np.diff(arr4, n = 2)
print(c)