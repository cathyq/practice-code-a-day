# Problem from Hackerrank contest
# https://www.hackerrank.com/contests/w30/challenges/melodious-password
#!/bin/python

import sys
import itertools

n = 6 # 1<=n<=6

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxz'
outer = 0
inner = 0
if n % 2 == 0:
    outer = inner = n/2
else:
    outer = n/2
    inner = outer+1
for v in itertools.product(vowels, repeat=outer):
    for c in itertools.product(consonants, repeat=inner):
        print ''.join(''.join(x) for x in itertools.izip_longest(c, v, fillvalue=''))
for c in itertools.product(consonants, repeat=outer):
    for v in itertools.product(vowels, repeat=inner):
        print ''.join(''.join(x) for x in itertools.izip_longest(v, c, fillvalue=''))
