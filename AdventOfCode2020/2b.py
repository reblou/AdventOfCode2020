import re

file = open("2.txt", "r")
lines = file.readlines()

valid = 0

for l in lines:
	m = re.match("(\d+)-(\d+) ([a-z]): ([a-z]*)", l)
	print(m.groups())
	pos1 = int(m.group(1)) - 1
	pos2 = int(m.group(2)) - 1
	letter = m.group(3)
	password = m.group(4)

	count = 0

	if (password[pos1] == letter) ^ (password[pos2] == letter):
		print("valid only one pos is letter" + l)
		valid += 1

print("Total valid: " + str(valid))

