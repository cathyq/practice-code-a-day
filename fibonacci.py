# Given an integer, write the fibonacci function.
# problem from ctci

def fibonacci(n):
    # Write your code here.
    if n == 0: 
        return 0
    a = 0
    b = 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    return a + b

n = 3
print(fibonacci(n))