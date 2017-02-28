#!/bin/python

# Every letter has its own height. For a given string, find the area covering the string (width of string x maxheight)

# Problem from Hackerrank

import sys


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,5]
word = 'abc'

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d = {}
for i in range(len(letter)):
    d[letter[i]] = h[i]
#print d


maxHeight = 1
for j in word:
    if j in d:
        if d[j] > maxHeight:    
            maxHeight = d[j] 
        #print d[j]
#print maxHeight 


area = len(word) * maxHeight 
print area