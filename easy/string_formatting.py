# Given an integer, print Decimal, Octal, Hexadecimal, and Binary for each integer i from i to n.
# Problem from Hackerrank

from __future__ import print_function

n = 17 # an integer

w = len(bin(n)[2:])

for i in range(1, n+1):
    print (str(i).rjust(w, " "), str(oct(i)[1:]).rjust(w, " "), str(hex(i)[2:]).upper().rjust(w, " "), str(bin(i)[2:]).rjust(w, " "), sep = " ")