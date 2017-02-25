def mean(a):
	print "Finding average of {0}".format(a)
	sum_value = 0.0
	for i in range(0, len(a)):
		sum_value += a[i]
		print "Loop value {0}, sum_value {1}, a value {2}".format(i, sum_value, a[i])
	
	m = sum_value / len(a)
	return m

def median(a):
	print "Finding median of {0}".format(a)
	a.sort()
	print "Finding median of SORTED {0}".format(a)
	
	if len(a) % 2 == 0:
		print "Array is even in length"
		half = len(a) / 2 # if 10 elements, half=5
		print "Half is {0}".format(half)
		avg = (a[half] + a[half-1]) / 2
		return avg
	else:
		print "Array is odd in length"
		half = len(a) / 2
		print "Half is {0}".format(half)
		return a[half]

def mode(a):
	print "Finding mode of {0}".format(a)
	a.sort()
	print "Finding mode of SORTED {0}".format(a)

	currentValue = 0
	currentCount = 0

	for i in range(0, len(a)):
		if currentValue != a[i]: # reset because we changed values
			currentCount = 0 

		currentValue = a[i]
		print "currentValue {0}".format(currentValue)

		currentCount += 1
		print "currentCount {0}".format(currentCount)


		# if currentCount < nextCount:
		# 	return nextCount
		# else:
		# 	return currentCount




##### DO NOT WRITE BELOW THIS LINE #####
a = [2,1,6,10,2,20] # len(a) = 11
print mean(a)
print median(a)
print mode(a)
# print range_value(a)


# ex = [1, 2, 2, 6, 10, 20]
# i = 0
# a[0] = 1
# currentValue = 1
# currentCount = 0



