# https://www.hackerrank.com/contests/womens-codesprint-3/challenges/the-birthday-bar
# Problem from Hackerrank Women's CodeSprint 3
#!/bin/python

import sys


n = 5
squares = [1,2,1,3,2]
d,m = [3,2]
# your code goes here

total = 0


for i in range(n-m+1):
    subtotal = 0
    for t in range(m):
        subtotal += squares[t+i]
    if subtotal == d:
        total += 1
print total