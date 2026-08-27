# we can create our own ufunc
# we use frompyfunc() method: takes function, inputs, output 

import numpy as np

def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1) # Here 2 means 2 inputs and 1 means single output

print(myadd([1,2,3,4],[5,6,7,8]))

print(type(myadd))

