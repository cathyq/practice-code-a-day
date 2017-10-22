# Gets k and the input arr
k, arr = int(input()), list(map(int, input().split()))

# Creates a set out of the arr. We sum the set and multiply
# by k to get the sum if every room number appeared k times.
# Subtracting the sum of the input arr leaves k-1 repeats
# of the captain's room number, so we divide by k-1
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))
