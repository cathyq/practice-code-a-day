# Given a string s, and a number k, encrpt s such that s rotates every leter by K. Retrun the encript string. 
# Problem from Hackerrank
#!/bin/python

import sys


n = 12
s = 'Hello_World!'
k = 4

new = []
strs = 'abcdefghijklmnopqrstuvwxyz'      
strs_cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for i in range(n):                     
    if s[i] in strs:                
        new.append(strs[(strs.index(s[i]) + k) % 26]) 
    elif s[i] in strs_cap:
        new.append(strs_cap[(strs_cap.index(s[i]) + k) % 26])
    else:
        new.append(s[i])          
print ''.join(new)