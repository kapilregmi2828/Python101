# lcm lowest common multiple

import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1,num2)
print(x)

arr = np.array([3,6,9]) # array
a = np.lcm.reduce(arr)
print(a)

arr2 = np.arange(1,11) # Range
b = np.lcm.reduce(arr2)
print(b)


# GCD greatest common divisor or Highest common factor

num3 = 6
num4 = 9

c = np.gcd(num3,num4)
print(c)

arr3 = np.array([20,8,32,36,16]) # Range
d = np.gcd.reduce(arr3)
print(d)