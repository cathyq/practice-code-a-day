# Problem from hackerrank: https://www.hackerrank.com/challenges/merge-the-tools
# Method 1
def merge_the_tools(string, k): 
    sub = len(string)/k
    new = []
    for i in list(string):
        new.append(i)
        if len(new) == k:
            noDupes = []
            [noDupes.append(i) for i in new if i not in noDupes]
            result = "".join(list(noDupes))
            print result
            new[:] = []


print "Test 1"
string = "AABCAAADA"
k=3
merge_the_tools(string, k)
print

# method 2
def merge_the_tools(string, k): 
    new = []
    seen = {}
    for index, i in enumerate(list(string)):
        if i not in seen:
            seen[i] = True
            new.append(i)
        if (index+1)%k == 0:
            print "".join(new)
            new = []
            seen.clear()

print "Test 2"
string = "AABCAAADA"
k=3
merge_the_tools(string, k)
