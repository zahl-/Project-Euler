import math
largest = 0
largest_line = 0
with open("p099_base_exp.txt", "r") as f:
	linenum = 1
	for line in f:
		list = line.split(',')
		value = int(list[1]) * math.log(int(list[0]))
		if value > largest:
			largest = value
			largest_line = linenum
		linenum += 1

print largest_line
		
