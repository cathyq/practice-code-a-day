# Find out if the words in the ransom note can be duplicated from words in the magazine. Print 'yes' if it can, 'no' if it can not.
# Problem from cracking the code interview

m, n = 6, 4
magazine = 'give me one grand today night'
ransom = 'give one grand today'

def ransom_note(magazine, ransom):
    d = {}
    for i in magazine:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for j in ransom:
        if j in d and d[j] > 0:
            d[j] -= 1
        else:
            return False
        
    return True
    
    
answer = ransom_note(magazine, ransom)

if(answer):
    print "Yes"
else:
    print "No"