sum = 0
for x in range(1, 1002, 2):
	sum += x**2
	if x > 1:
		sum += x**2 - (x - 1)
		sum += x**2 - 2*(x - 1)
		sum += x**2 - 3*(x - 1)
print sum
