#recursive solution is painfuly slow... don't do it
def fib(x):
	if (x == 1):
		return 0
	if (x == 2):
		return 1
	return fib(x-1) + fib(x-2)

minus1 = 1
fib = 1
sum = 0

while (fib < 4000000):
	hold_fib = fib
	fib = fib + minus1
	minus1 = hold_fib
	if (fib % 2 == 0):
		sum += fib

print (sum)

