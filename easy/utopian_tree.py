#!/bin/python
# The Utopian Tree goes through 2 cycles of growth per year. 
# Every summer, its height increases by 1 meter. Every spring, it doubles in height.
# Problem is from Hackerrank.
# h= height, n=list of number of cycles. 

import sys


h = 1
n = [0,1,4]
for k in n:
    if k == 0:
        print 1
    elif k == 1:
        print 2
    elif k % 2 == 0:
        for i in range(k/2):  
            h = h*2+1      
        print h
    else:
        for i in range(k/2):     
            h = h*2+1
        print h*2   
         
    #for i in range(n/2):     
    #    h = h*2+1   
    #    if n % 2 != 0:
    #        print h*2
    #    else:
    #        print h