# Given n numbers, find the second largest number.
# Problem from Hackerrank
# n=number of intergers, a=array
n = 5
a = [2,3,6,6,5]


# METHOD 1
a = set(a)
a.remove(max(a))
print max(a)


# METHOD 2
maxNumber = max(a)
while max(a) == maxNumber:
    a.remove(maxNumber)
print max(a)
