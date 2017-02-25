
# Check if the string is funny. Funny if string s[i]-s[i-1] = r[i]-r[i-1] 
# s = string, r = reverse of a string
# This problem is from HackerRank 

s_arr = ['acxz', 'bcxz'] # an array of stings

def funny(s):    
    r = s[::-1]
    for i in range(1, len(s)-1):
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(r[i])-ord(r[i-1])):
            return False         
    return True


for i in s_arr: 
    if funny(i):
        print "Funny"
    else:
        print "Not Funny"

