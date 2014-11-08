sum = 0
with open("Problem013.txt", "r") as f:
	for line in f:
		sum += int(line)
print str(sum)[:10]
