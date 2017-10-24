#Pangrams: sentences constructed by using every letter of the alphabet at least once.
#From Hackerrank

s = 'We promptly judged antique ivory buckles for the prize'    

s = "".join(s.split())
s = s.lower()

#alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def pangram(s):

    
    for i in alphabet:
    	if i not in s:
            return False    
    return True

if pangram(s):
    print 'pangram'
else:
    print 'not pangram'

