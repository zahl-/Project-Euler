'''
This problem can be solved with combinatorics.
Note that to reach the bottom right you must go right 20 times and down 20 times, and order does not matter
There are 40 moves in total, and finding how many ways to go right (or down) is equivalent to finding out how many total ways there are

so, 20 choose 40 is the answer. the amount of ways to pick 20 down movements out of 40 spots
'''
import math
def choose(n, r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

print choose(40, 20)
