# copy is a new array. it owns the data so any changes made to the copy will not affect original array and vice-versa.
# view is just a view of original array. so any changed made to the view will affect the original array and vice-versa. 

import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x) # deosnt change the copy even if the original is modified 

y = arr.view()
print(y) # changes the view since the original is modified. 
print(arr)

# base attributes returns None is the array owns the data otherwise returns original object. 

print(x.base) # None
print(y.base) # [42 2 3 4 5]