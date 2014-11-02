import math

sum = 0
sum_squares = 0

for n in range(1, 101):
	sum += n
	sum_squares += math.pow(n, 2)

sum_squared = math.pow(sum, 2)
difference = int(sum_squared - sum_squares)
print(difference)
