fib_prev = 1
fib = 1
count = 2
while fib <= 10**999:
	fib_temp = fib
	fib = fib + fib_prev
	fib_prev = fib_temp
	count += 1

print count
	
