# Given an n-element array, sort it using Bubble Sort algorithm in ascending order.
# problem from CTCI

n = 3
a = [1,2,3]

numSwaps = 0
for j in range(n):
    
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numSwaps += 1
    
    if numSwaps == 0:
        break

print "Array is sorted in %d swaps." % (numSwaps)    
print "First Element: %d" % a[0]
print "Last Element: %d" % a[-1]