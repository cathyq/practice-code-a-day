x = "I love New York City. It's the best city for pandas."


def count_letter(letter, file):
	sum = 0
	file = file.lower()
	letter = letter.lower()
	for i in range(0, len(file)):
		if file[i] == letter:
			sum	+= 1	
	return sum

print count_letter('i', x) # should print 4
print count_letter('a', x) # should print 2
print count_letter('N', x) # should return 2