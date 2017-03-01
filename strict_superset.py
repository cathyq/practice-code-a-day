# Find out if set A is a strict superset of set B.
# A strict superset has at least one element that does not exist in its subset.

# Problem from Hackerrank

A = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 84, 78])
B = set([1,2,3,4,5])
N = 2

isStrict = True
for i in B:
    if len(B) != len(A.intersection(B)):
        isStrict = False
        break

print isStrict