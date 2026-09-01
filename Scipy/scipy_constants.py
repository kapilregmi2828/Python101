# Scipy is a Python toolbox that helps to solve difficult math, science, statistics and engineering problems.

from scipy import constants
from scipy.optimize import root
from math import cos
import numpy as np
print(constants.liter)

print(constants.pi)

#print(dir(constants))

# Scipy optimizer: best minimum value of a function
def eqn(x):
    return x + np.cos(x)

myroot = root(eqn, 0)
print(myroot.x)
