import re

file = open("2.txt", "r")
lines = file.readlines()

valid = 0

for l in lines:
	m = re.match("(\d+)-(\d+) ([a-z]): ([a-z]*)", l)
	print(m.groups())
	min = int(m.group(1))
	max = int(m.group(2))
	letter = m.group(3)
	password = m.group(4)

	count = 0
	for p in password:
		if p == letter:
			count += 1

	if (count >= min and count <= max):
		print("valid: " + l)
		valid += 1

print("Total valid: " + str(valid))

