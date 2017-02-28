# Reduce a given string - delete the sting's adjacent letter with the same value. 

s = 'aaabbbcdfffff'

dups = True
while dups:
    dups = False
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            s = s[0:i-1] + s[i+1:]
            dups = True
            break

if s == "":
    print "Empty String"
else:
    print s