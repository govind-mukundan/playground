# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:44:38 2018

@author: Govind
"""

# NOTE: With numpy often the submatrices and sliced elements are all references to the 
# original matrix (not new copies), so if you modify them you'll end up modifying the source matrix
# This is in contrast to Pandas Data Frame operations where most of the time you get copies

# https://docs.scipy.org/doc/numpy/user/quickstart.html
# Detailed tutorial: http://www.scipy-lectures.org/intro/numpy/index.html

import numpy as np
print(np.__version__)

# Create a two-dimensional array of size 3 rows x 4 columns:
B = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])

# Conventional list
C =           [[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]]
print(B)
print(B.dtype)
# print(C.dtype)  -- Doesn't exist for list object

print(B.ndim) # Number of dimensions
print(B.shape) # Matrix shape
print(len (B)) # length of 1st dimension

# Special matrices - By default the dtype is double / float64
print(np.zeros((3, 4)))
print(np.ones((3, 4)))
print(np.eye(3))
print(np.diag([1, 2, 3]))
A = np.empty((3, 4)) # An "empty" 3 x 4 matrix
print(A)

e = np.eye(3)
print(e.dtype)

np.array ([2, 12, 22, 32, 42, 52])

############# Slicing and Indexing ##################

# Follows general python slicing rules - 
# SLICE - https://www.programiz.com/python-programming/methods/built-in/slice
# [Start : Stop : Step] --> Slicing stops at (STOP -1)

Z = np.array([np.arange(0, 6),              # [0,1,2,3,4,5]
                       np.arange(10, 16),
                       np.arange(20, 26),
                       np.arange(30, 36),
                       np.arange(40, 46),
                       np.arange(50, 56)])

# MultiD arrays can be indexed in either the [row,column] form or [row][column] form
Z[0,0::2]       # Every alternate element in row - 0 => i.e. Multiples of 2
Z[0][0::2]      # Every alternate element in row - 0 => i.e. Multiples of 2
Z[::-1]         # Reverse the ROWS
Z[:,::-1]       # Reverse the COLUMNS
Z[::-1,::-1]    # Reverse the ROWS and COLUMNS


# Slices are *references* to the original array => they share memory
Z_slice = Z[0,0::2]
Z_copy = Z[0,0::2].copy()

print ("Z and Z_slice share memory: %s" % np.may_share_memory (Z, Z_slice))
print ("Z and Z_copy share memory: %s" % np.may_share_memory (Z, Z_copy))

# The indices may be provided as an array too, an array of BOOLs is also allowed
# NOTE: the DIMENSION of the INDEX ARRAY *must* MATCH that of the source array
# For example, you can't use Z[indx] here

indx = np.array([True, False, True, False, True, False])
alt_0 = Z[0][indx]

indx = np.array([0,2,4])
alt_1 = Z[0][indx]

assert (alt_0 == alt_1).all() and (alt_0 == Z[0,0::2]).all()

# Multiple elements may be assigned at once
Z[0] = True
print(Z[0])

######## SPARSE MATRICES ##############################
import numpy as np
import pandas as pd
from random import sample # Used to generate a random sample
from IPython.display import display

# Sparse matrices are matrices where most of the values are 0, so instead of allocating memory for default values
# you store the matrix as a dictionary with Tuples of (row_index, col_index) as Keys and the value being the value 
# of the matrix element at that (row,col)
# Eg: A vector of 100 entries = [1, 0, 0, ... 20] can be stored as dictionary = {(0,1):1, (0,200):20}
# eg: http://interactivepython.org/runestone/static/CS152f17/Dictionaries/Sparsematrices.html

# The below setup stores them as nested default dictionaries
# Allowing indexing of the form A[0][1]
# eg:
# {0: defaultdict(float, {1: -2.5, 2: 1.2}),
# 1: defaultdict(float, {0: 0.1, 1: 1.0}),
# 2: defaultdict(float, {0: 6.0, 1: -1.0})})

def sparse_matrix(base_type=float):
    """Returns a sparse matrix using nested default dictionaries."""
    from collections import defaultdict
    return defaultdict(lambda: defaultdict (base_type))

def dense_vector(init, base_type=float):
    """
    Returns a dense vector, either of a given length
    and initialized to 0 values or using a given list
    of initial values.
    """
    # Case 1: `init` is a list of initial values for the vector entries
    if type(init) is list:
        initial_values = init
        return [base_type(x) for x in initial_values]
    
    # Else, case 2: `init` is a vector length.
    assert type(init) is int
    return [base_type(0)] * init



# Test cell: `spmv_baseline_test`

#   / 0.   -2.5   1.2 \   / 1. \   / -1.4 \
#   | 0.1   1.    0.  | * | 2. | = |  2.1 |
#   \ 6.   -1.    0.  /   \ 3. /   \  4.0 /

A = sparse_matrix ()
A[0][1] = -2.5
A[0][2] = 1.2
A[1][0] = 0.1
A[1][1] = 1.
A[2][0] = 6.
A[2][1] = -1.

x = dense_vector ([1, 2, 3])
y0 = dense_vector ([-1.4, 2.1, 4.0])


# Try your code:
#y = spmv(A, x)

max_abs_residual = max([abs(a-b) for a, b in zip(y, y0)])

print ("==> A:", A)
print ("==> x:", x)
print ("==> True solution, y0:", y0)
print ("==> Your solution, y:", y)
print ("==> Residual (infinity norm):", max_abs_residual)
assert max_abs_residual <= 1e-14

print ("\n(Passed.)")

np.arange(10)

## VECTORS and MATRIX operations
# All vectors and matrix operations are to be done using np.array(). Using np.matrix() is discouraged
# See: https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html
# A summary of the differences is here --> https://docs.scipy.org/doc/numpy-1.15.0/user/numpy-for-matlab-users.html
# Matrices are *ALWAYS* 2D arrays in numpy -> if you want to represent a column or row matrix always use 2D a shape of (1,N) or (N,1)

# The best way to create multi-dimensional arrays without brain pain is to start with a single dimension and create multi-D views into it
x = np.array([1,2,3,4,5,6])
# Note that the product of dimensions of all the reshape() operations is constant

x.reshape(3,2)
#Out[11]: 
#array([[1, 2],
#       [3, 4],
#       [5, 6]])

x.reshape(2,3)
#Out[12]: 
#array([[1, 2, 3],
#       [4, 5, 6]])

x.reshape(3,1,2)   # 3x1 Matrix of 2D vectors
#Out[13]: 
#array([[[1, 2]],
#
#       [[3, 4]],
#
#       [[5, 6]]])

x.reshape(2,1,3)
#Out[14]: 
#array([[[1, 2, 3]],
#
#       [[4, 5, 6]]])

# Another way to add dimensions without reshape() is to use the "None" index
x[:,None]     # -> Column vector
#Out[40]: 
#array([[1],
#       [2],
#       [3],
#       [4],
#       [5],
#       [6]])

x.reshape(len(x),1) # -> Column vector
#Out[41]: 
#array([[1],
#       [2],
#       [3],
#       [4],
#       [5],
#       [6]])

x[:,None, None] # -> Column matrix of 1D vectors
#Out[42]: 
#array([[[1]],
#
#       [[2]],
#
#       [[3]],
#
#       [[4]],
#
#       [[5]],
#
#       [[6]]])

y
#Out[43]: 
#array([[1, 2, 3],
#       [4, 5, 6]])

y[:,:,None]
#Out[44]: 
#array([[[1],
#        [2],
#        [3]],
#
#       [[4],
#        [5],
#        [6]]])

# np.resize() can give you a new array with a new shape and size
z = np.array([1,2])
np.resize(z, (1,4))
#Out[37]: array([[1, 2, 1, 2]])

np.resize(z, (1,3))
#Out[38]: array([[1, 2, 1]])

# ROW and COLUMN vectors

a = np.array([1,2,3])

a.T   # The transpose of a 1D array is the same array
#Out[18]: array([1, 2, 3])

a = np.array([[1,2,3]])

a.T   # The transpose of a 2D array has it's shape changed as expected
#Out[20]: 
#array([[1],
#       [2],
#       [3]])

# ACHTUNG: Extracting a Column vector from a matrix
# By default when you extract a column from a matrix using the M[:, 2] syntax, you get a 1D array which is equal to a ROW
# To get it back as a coumn you have to use the M[:, 2:3] slice syntax

A = np.array ([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]
              ], dtype=float)

print ("A[:, :] ==\n", A)
print ("\na0 := A[:, 0] ==\n", A[:, 0])
print ("\na1 := A[:, 2:3] == \n", A[:, 2:3])

# alternatively you have to reshape A[:,0] into a 2D array to get a column vector

## COOL stuff

# Replace all elements > 0 with 0
a = np.array([1,2,3,-4])  # Does not work with python lists!
a[a > 0] = 0

a
#Out[68]: array([ 0,  0,  0, -4])

x = np.array([1,2,3,4])
x > 2
#Out[251]: array([False, False,  True,  True])

x == 4
#Out[252]: array([False, False, False,  True])



## AXIS
# Axis especially with respect to the np.sum() function refers to the dimension along which the sum() will be calculated
# i.e. axis = 0 means that we are going to extract all the row objects from the array, stack them together and perform an element wise sum over them
# axis = 1 => extract all the axis = 1 => column elements, stack them together and perform an element wise sum over them
# axis = -1 => means the last axis

y = np.array([[1, 2, 3], 
              [4, 5, 6]])
    
np.sum(y, axis = 0)
#Out[23]: array([5, 7, 9])

np.sum(y, axis = 1)
#Out[28]: array([ 6, 15])

np.sum(y)
#Out[46]: 21

## CONCATENATION
# vstack and hstack for 1D - 3D arrays
a = np.array([1, 2, 3])

b = np.array([2, 3, 4])

np.vstack((a,b))  # Input is a TUPLE
#array([[1, 2, 3],
#       [2, 3, 4]])

# General concatenation - concatenate, stack and block ==> These accept a sequence of array_like as input
>>> np.stack((a, b))
array([[1, 2, 3],
       [2, 3, 4]])

## Array Broadcasting


## DOT/Inner Product
# A unique feature of np is that for 1D arrays you don't have to care about whether they are "column" or "row" vectors
# when performing the dot product. You can just directly calculate the inner product
x.dot(x)
#Out[74]: 153.8905

# You can check the dimensions of an array by looking at the ndim property
x.ndim

# When dealing with 2D arrays, you *must* worry about their shape


# https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.sort.html
## SEARCHING
# Find indices that satisfy a condition
x = [50, 60, 70]
np.where(x>55)
np.argwhere(x>55)

y = np.array([[1, 2, 3], 
              [4, 5, 6]])
              

np.where(y==6)
#Out[189]: (array([1], dtype=int64), array([2], dtype=int64))

np.argwhere(y==6)
#Out[190]: array([[1, 2]], dtype=int64)

# Assign multiple indices in one line
x[[0,1]] = 0

# SORTING
# sort() sorts the values
# argsort() is useful when you want to know the index of the sorted values