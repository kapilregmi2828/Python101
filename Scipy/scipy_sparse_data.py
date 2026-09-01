# sparse data is data that has mostly unused elements. 
# It is a dataset where most of the values are zero.
# Dense array is the opposite of sparse. 

# create a CSR (Compressed Sparse Row) matrix from an array

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(arr))

arr2 = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr2))

print(csr_matrix(arr2).data)

print(csr_matrix(arr2).count_nonzero())  #count_nonzero() method counts non-zeros

mat = csr_matrix(arr2)
mat.eliminate_zeros()
print(mat)

