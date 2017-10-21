from collections import Counter

k = int(input())
rooms = input().split()
c = dict(Counter(rooms))
for key, value in c.items():
    if int(value) != k:
        print(key)
