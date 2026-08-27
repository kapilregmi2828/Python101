# ufuncs means Universal Functions. It is a math machine that can work on an entire array at once. 

# without ufunc, we use built-in zip() method
import numpy as np
x = [1,2,3,4,2,9]
y = [4,5,6,7,8]
z = []

for i,j in zip(x,y):
    z.append(i+j)

print(z)

a = [1,2,3,4,5]
b = [4,5,6,7]
c = np.add(a,b)
print(c)