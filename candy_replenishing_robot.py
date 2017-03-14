# https://www.hackerrank.com/contests/w30/challenges/candy-replenishing-robot
# Problem from Hackerrank competition

n = 8
t = 4
c = [3,1,7,5]
i = 0
count = 0
remain = n
while i < t-1:
    remain -= c[0]
    if remain < 5:
        count += (n-remain)
        remain += (n-remain)
    c.pop(0)
    i += 1
print count    