# https://www.hackerrank.com/contests/w30/challenges/range-modular-queries
# problem from hackerrank contest
#!/bin/python

import sys


n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
a = map(int, raw_input().strip().split(' '))
for a0 in xrange(q):
    left,right,x,y = raw_input().strip().split(' ')
    left,right,x,y = [int(left),int(right),int(x),int(y)]
    
    count = 0
    for i in range(left, right+1):
        if a[i] % x == y:
            count += 1
    print count