x = int(raw_input())
y = raw_input()
s = set(y)
s.pop()
num = len(s)
for i in range(num):
    if y.count(list(s)[i]) != x:
        print list(s)[i]

