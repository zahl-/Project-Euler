def isPalindromic(number):
	string = str(number)
	return string == string[::-1]
	
largest = 0
for x in range(100, 1000):
	for y in range(x, 1000):
		product = x * y
		if (product > largest and isPalindromic(product)):
			largest = product
print(largest)
