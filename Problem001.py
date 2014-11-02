count = 0
for x in range(1, 1000):
	if (x % 3 == 0):
		count += x
	if (x % 5 == 0):
		count += x
	if (x % 15 == 0):
		count -= x
print(count)
