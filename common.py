import math

class primality:
	def __init__(self):
		self.primelist = [2]
		self.primecount = 1

	def listprimes(self, limit):
		number = 3
		while (self.primecount != limit):
			if(self.isprime(number)):
				self.primelist.append(number)
				self.primecount += 1
			number += 2

	def sieveprimes(self, limit):
		sieve = [True] * (limit+1)
		sieve[0] = False
		sieve[1] = False
		sqrt = math.sqrt(limit)
		floor = math.floor(sqrt)
		bound = int(floor)
		for n in range(0, bound+1):
			if (sieve[n]):
				for x in range(int(math.pow(n, 2)), limit+1, n):
					sieve[x] = False
		primes = []
		count = 0
		for x in sieve:
			if (x):
				primes.append(count)
			count += 1			
		return primes
			

	def isprime(self, number):
		sqrt = math.sqrt(number)
		sqrt_int = int(math.floor(sqrt))
		prime = True
		for x in self.primelist:
			if (number % x == 0):
				prime = False
				break

		return prime
