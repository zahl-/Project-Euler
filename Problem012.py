import math

found = False
num = 0
while not found:
	num += 1
	trinum = num * (num+1)/2
	divisors = 2
	for x in range(1, int(math.floor(math.sqrt(trinum)))):
		if trinum % x == 0:
			divisors += 2
		if divisors > 500:
			found = True
print trinum
