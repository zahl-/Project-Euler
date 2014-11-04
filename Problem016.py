import math

num = int(math.pow(2, 1000))
sum = 0

while (num >= 1):
	mod = num % 10;
	sum += mod
	num /= 10

print (sum)
