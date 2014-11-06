import time
start = time.clock()
largest = 0
for x in range(1, 101):
	for y in range(1, 101):
		exp = x ** y
		sum = 0
		while exp >= 1:
			exp, rem = divmod(exp, 10)
			sum += rem
		if sum > largest:
			largest = sum

print largest 
print time.clock() - start

