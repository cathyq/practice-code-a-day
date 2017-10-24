#!/bin/python
# Insertion Sort 
# Problem from Hackerrank
# m=size of array, ar=unsorted array

m = 5
ar = [2,4,6,8,3]

def insertionSort(ar):  
    pivot = ar[-1]
    for i in reversed(range(len(ar)-1)):   
        if ar[i] > pivot:
            ar[i+1] = ar[i]                   
        elif ar[i] <= pivot:
            ar[i+1] = pivot
            break
        for j in ar: print j,
        print
        
        if i == 0:
            ar[i] = pivot
                       
    for k in ar: print k,
    
     
    return ar 
     
    
insertionSort(ar)