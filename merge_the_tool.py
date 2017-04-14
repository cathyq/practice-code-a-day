# Problem from hackerrank: https://www.hackerrank.com/challenges/merge-the-tools
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

string = "AABCAAADA"
k=3
merge_the_tools(string, k)