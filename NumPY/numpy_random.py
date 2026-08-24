# Random doesnt mean a different number everytime. random means something that cannot be predicted logically. 

# Generate a random number from 0-100:
from numpy import random
x = random.randint(100)
print(x)

# Generate a random float between 0-1:
y = random.rand()
print(y)

# Generate a 1-D array of 5 random int from 0-100:

a = random.randint(100, size=(5))
print(a)

# generate a 2-d array of 5 random int from 0-100:
b = random.randint(100, size = (3,5))
print(b)

# 1-D array of float

c = random.rand(5)
print(c)

# 2-D array of float

d = random.rand(3,5)
print(d)