import common

primer = common.primality()

count = 0

def leftPrime(primer, prime):
	p_string = str(prime)
	subPrime = True
	while len(p_string) >= 1:
		p_string = p_string[1:]
		if p_string == "":
			break
		if not primer.isprime(int(p_string)):
			subPrime = False
			break
	return subPrime

def rightPrime(primer, prime):
	p_string = str(prime)
	subPrime = True
	while len(p_string) >= 1:
		p_string = p_string[0:-1]
		if p_string == "":
			break
		if not primer.isprime(int(p_string)):
			subPrime = False
			break
	return subPrime

count = 0
sum = 0
num = 10

while count < 11:
	if primer.isprime(num) and leftPrime(primer, num) and rightPrime(primer, num):
		print num
		sum += num
		count += 1
	num += 1
print sum

