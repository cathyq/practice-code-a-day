# Anagrams: if the first string's letters can be rearranged to form the second string. Both need to contain the same letters & same frequency. For example, 'bacdc' and 'dcbac' are anagrams, but 'bacdc' and 'dcbad' are not.
# Hackerrank problem.
# Given two strings, find out the minimum number of charater deletions to make them anagrams.

from collections import Counter

a = 'cde' # delete d and e to get c
b = 'abc' # delete a and b to get c

count = Counter(a)
count.subtract(b)
print sum(abs(i) for i in count.values())