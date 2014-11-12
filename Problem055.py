def isPalindrome(string):
	return string == string[::-1]

lychrel_count = 0
for x in range(1, 10001):
	sum = x + int(str(x)[::-1])
	lychrel = True
	for y in range(1, 51):
		if isPalindrome(str(sum)):
			lychrel = False
			break
		else:
			sum += int(str(sum)[::-1])
	if lychrel:
		lychrel_count += 1

print lychrel_count

