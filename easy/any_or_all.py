# You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
# Problem from Hackerrank
ar = [12, 9, 61, 5, 14]

def palindormic(ar):
    lst = []
    for i in ar:
        mystr = str(i)
        for j in range(len(mystr)):   
            ispal = True
            if mystr[j] != mystr[len(mystr)-1-j]:
                ispal = False
                lst.append(False)
                break
        if ispal is True: lst.append(True)   
    return lst

if all(i > 0 for i in ar) and any(palindormic(ar)) is True:
    print True
else:
    print False