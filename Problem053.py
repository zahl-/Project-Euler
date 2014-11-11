import math
def nCr(n, r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

count = 0
for x in range(1, 101):
	for y in range(1, x+1):
		if nCr(x, y) > 1000000:
			count += 1

print count	
