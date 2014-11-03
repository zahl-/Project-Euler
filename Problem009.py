import math


'''	BAD BRUTE FORCE SOLUTION
for a in range(2, 1000):
	for b in range(2, 1000):
		for c in range(2, 1000):
			pythag = (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2))
			if (pythag):
				py_sum = a + b + c
				if (py_sum == 1000):
					triple = (a, b, c)
					product = a*b*c

print (triple, product)
'''


'''
	Note that some pythagorean triples (but not all) can be generated by positive integers n > m such that:
	a = m^2 - n^2
	b = 2mn
	c = m^2 + n^2
	(from Euclid's Elements), now represent a, b, and c as such:
	a + b + c = x
	2(m^2) + 2mn = x
	m^2 + 2mn - (1/2)x
	Quadratic formula:
	m = -n +- sqrt(n^2 - 2x)

	now enumerate over the naturals from 0 to the sum for each n, solve until two positive integer solutions are found. 
	
'''

def findTriple(sum):
	m = 0
	for n in range(0, sum):
		delta = math.pow(n, 2) + 2*sum
		m1 = (-n + math.sqrt(delta)) / 2
		m2 = (-n - math.sqrt(delta)) / 2
		m = m1 if (m1.is_integer() and m1 > n) else 0
		m = m2 if (m2.is_integer() and m2 > n) else m
		if (m != 0):
			return [int(2*m*n), int(math.pow(m, 2) - math.pow(n, 2)), int(math.pow(m, 2) + math.pow(n, 2))]

triple = findTriple(1000)
print(triple, triple[0]*triple[1]*triple[2])