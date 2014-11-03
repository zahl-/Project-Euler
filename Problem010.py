import math
import common

primer = common.primality()
primes = primer.sieveprimes(2000000)
print(primes)
sum = 0
for x in primes:
	sum += x

print(sum)

