# Problem from Hackerrank contest 
# https://www.hackerrank.com/contests/w30/challenges/find-the-minimum-number

#!/bin/python

import sys


n = 5
#s = 'min(int, int)'

def min_number(n):
    if n == 2:
        return 'min(int, int)'
    else:
        return "min(int, " + (min_number(n-1)) + ")"
                
print min_number(n) 