longest = 0
starting = 0
for x in range(1, 1000000):
	collatz = x
	count = 1
	while collatz != 1:
		if collatz % 2 == 0:
			collatz /= 2
		else:
			collatz *= 3
			collatz += 1
		count += 1
	if count > longest:
		longest = count
		starting = x

print starting
