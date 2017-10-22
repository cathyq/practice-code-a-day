# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
import sys

k = int(sys.stdin.readline())
rooms = sys.stdin.readline()

def find_captain(k, rooms):

    c = collections.Counter()
    for num in rooms:
        c[num] += 1

    for key, value in c.iteritems():
        if value < k:
            sys.stdout.write(key)


find_captain(k, rooms)
