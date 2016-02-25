# Given a string, find out if all the characters in the string are unique.#
# False = NOT unique, duplicate
# True = Unique

# Runtime: O(n^2)

def stringReturn(x):
	for i in range(0, len(x)):
		for j in range(i+1, len(x)):
			if x[i] == x[j]:
				return False
	return True

print stringReturn("bcdefghijklmnopaz")
print stringReturn("ab")
print stringReturn(" ")
print stringReturn("  ")
print stringReturn("11")

print "Better Version"
# Better version 
# Runtime: O(n)
# Space: O(n)

def stringHash(x):
	D = {}
	for i in range(0, len(x)):
		D[x[i]] = True
	for i in range(0, len(x)):
		if D[x[i]] == True:
			D[x[i]] = False
		else:
			return False
	return True

print stringHash("aacdefghijklmnopqrstuvwxyz") # a=False, b=False, c=True
print stringHash("abdc")





