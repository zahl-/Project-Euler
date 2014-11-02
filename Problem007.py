import math

def isprime(number, primelist) :
	sqrt = math.sqrt(number)
	sqrt_int = int(math.floor(sqrt))
	prime = True
	for x in primelist:
		if (number % x == 0):
			prime = False
			break

	return prime

primecount = 1
number = 3
primelist = [2]
while (primecount != 10001):
	if(isprime(number, primelist)):
		primelist.append(number)
		primecount += 1
	number += 2

print(primelist[10000])
