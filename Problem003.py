import math

def isprime(number) :
	sqrt = math.sqrt(number)
	sqrt_int = int(math.floor(sqrt))
	prime = True
	for x in range(2, sqrt_int+1):
		if (number % x == 0):
			prime = False
			break

	return prime

big_number = 600851475143
sqrt_bn = math.sqrt(big_number)
sqrt_int = int(math.floor(sqrt_bn))
factor = 0

for x in range(1, sqrt_int):
	if (big_number % x == 0 and isprime(x)):
		print (x)
		factor = x

print (factor)


	
