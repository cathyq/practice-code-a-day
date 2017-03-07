# Given an array of integers, find out if each integer is a prime or not a prime number.
# problem from ctci
import math

def isPrime(n):
    if n < 2:
        return "Not prime"
    else:
        for i in xrange(2, int(math.sqrt(n))):
            if n % i == 0:
                return "Not prime"            
        return "Prime"

k = [12, 5, 7]
for n in k:
    print isPrime(n)
