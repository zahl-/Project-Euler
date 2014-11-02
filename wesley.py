import math

def nCr(n, r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

sum = 0
for x in range(1, 19):
	sum += nCr(18, x)
	sum += nCr(20, x)
#sum += math.pow(2, 18)
print (sum)
