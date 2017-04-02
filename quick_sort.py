# QuickSort algorithm that prints every partitioned sub-array on a new line.
# problem from hackerrank
#!/bin/python
ar = [5, 8, 1, 3, 7, 9, 2]

def quick_sort(ar): 
    left = []
    right = []
    equal = []

    if len(ar) > 1:
        pivot = ar[0]
        for i in range(len(ar)):
            if ar[i] > pivot:
                right.append(ar[i])
            elif ar[i] < pivot:
                left.append(ar[i])
            else:
                equal.append(ar[i])
                
        result = quick_sort(left) + equal + quick_sort(right) 
 
        for j in result: print j,
        print
        return result
    else:
        return ar


quick_sort(ar)