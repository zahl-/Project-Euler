import math

num = math.factorial(100)
sum = 0

while (num >= 1):
	mod = num % 10;
	sum += mod
	num /= 10

print (sum)
