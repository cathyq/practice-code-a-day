# https://www.hackerrank.com/contests/womens-codesprint-3/challenges/ascii-flower
# problem from hackerrank contests
#!/bin/python

import sys

r,c = 2, 5


flower1 = [chr(46), chr(46), chr(79), chr(46), chr(46)]
flower2 = [chr(79), chr(46), chr(111), chr(46), chr(79)]
flower3 = [chr(46), chr(46), chr(79), chr(46), chr(46)]

f1 = "".join(flower1)
f2 = "".join(flower2)
f3 = "".join(flower3)

for r0 in range(r):
    line = ""
    for c0 in range(c):
        line += f1
    line += "\n"
    for c0 in range(c):
        line += f2
    line += "\n"
    for c0 in range(c):
        line += f3
    print line
    
'''
a = []
for i in range(r):
    a.append(t * c)
print a    
'''  

