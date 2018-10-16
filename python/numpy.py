# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:44:38 2018

@author: Govind
"""

# NOTE: With numpy often the submatrices and sliced elements are all references to the 
# original matrix (not new copies), so if you modify them you'll end up modifying the source matrix
# This is in contrast to Pandas Data Frame operations where most of the time you get copies

# https://docs.scipy.org/doc/numpy/user/quickstart.html

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

#### Slicing #####
# Follows general python sclicing rules - 
# SLICE - https://www.programiz.com/python-programming/methods/built-in/slice
# [Start : Stop : Step] --> Slicing stops at (STOP -1)

Z = np.array([np.arange(0, 6),
                       np.arange(10, 16),
                       np.arange(20, 26),
                       np.arange(30, 36),
                       np.arange(40, 46),
                       np.arange(50, 56)])

Z[0,0::2]       # Every alternate element in row - 0
Z[::-1]         # Reverse the ROWS
Z[:,::-1]       # Reverse the COLUMNS
Z[::-1,::-1]    # Reverse the ROWS and COLUMNS
