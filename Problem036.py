def isPalindromic(number):
	string = str(number)
	return string == string[::-1]

def dec_to_bin(x):
	return bin(x)[2:]

sum = 0
for x in range(1, 1000001, 2): # only check evens, an even number in base 10 will look like 1...0 in base 2, not a palindrome
	if isPalindromic(x):
		if isPalindromic(dec_to_bin(x)):
			sum += x 
	
print sum
