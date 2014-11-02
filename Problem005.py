'''
This is an instance of the problem of finding lcm(1, 2,... , n)
This sequence is defined in OEIS A03418 as
lcm(1,..., n) = PRODUCT(p^(log_p n)) for each prime p less than n
http://math.stackexchange.com/questions/302278/lcm1-2-3-n for more information
'''

import math

def isprime(number) :
	sqrt = math.sqrt(number)
	sqrt_int = int(math.floor(sqrt))
	prime = True
	for x in range(2, sqrt_int+1):
		if (number % x == 0):
			#print(number)
			prime = False
			break

	return prime

product = 1
for p in range(2, 21):
	if (isprime(p)):
		print(p)
		log_p_n = math.log(20, p)
		floor = math.floor(log_p_n)
		power = math.pow(p, floor)
		product *= int(power)


print(product)	
