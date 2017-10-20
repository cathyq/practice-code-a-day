import collections

k = int(input())
room_numbers = list(map(int, input().split()))

c = collections.Counter(room_numbers)
print (c.most_common()[-1][0])