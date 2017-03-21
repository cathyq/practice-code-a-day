# InsertionSort an unsorted array
# Problem from Hackerrank

#!/bin/python

s = 6
ar = [1,4,3,5,6,2]

def insertionSort(ar):
    for i in range(1,s):  
        pivot = ar[i]    
        while i > 0 and ar[i-1] > pivot:
            ar[i] = ar[i-1]
            i -= 1            
        ar[i] = pivot
        for j in ar: print j,
        print
        
    #for k in ar: return k
    return ar


insertionSort(ar)
