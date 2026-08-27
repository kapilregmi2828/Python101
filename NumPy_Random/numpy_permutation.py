# Permutation is the arrangement of an array. 
# There are 2 methods inn numpy to arrange an array
# shuffle() -- Makes chage to an original array
# permutation() -- doesnt change the original array

from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
random.shuffle(arr)
print(arr)
print("--------------------------")
arr2 = np.array([1,2,3,4,5])
print(arr2)
x= random.permutation(arr2)
print(x)