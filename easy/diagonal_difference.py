#!/bin/python

# Given a square matrix NxN, calculate the absolute difference between the sums of its diagonals.
# This problem is from hackerrank.

import sys


n_row = 3

a = [[11,2,4], [4,5,6], [10,8,-12]]
    
primary = 0
secondary = 0
for i in range(n_row):
    primary += a[i][i]

for j in range(n_row):
    secondary += a[j][n_row-j-1]
    
print abs(primary - secondary)