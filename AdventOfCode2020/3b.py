import numpy

file = open("3.txt", "r")
lines = file.readlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

slopetrees = []

for slope in slopes:
	r = slope[0]
	d = slope[1]
	print("For slope: " + str(r) + " " + str(d))
	trees = 0
	x = 0

	for i in range(d, len(lines), d):
		l = lines[i]
		trulen = len(l) -1
			
		if (x+r >= trulen):
			print("overflow from " + str(x) + " on line " + str(i))
			new = x + r - trulen
			print("new pos: " + str(new))
			x = new
		else:
			x+=r

		land = l[x]
		print(land)
		if land == "#":
			trees += 1
	print("Total trees: " + str(trees))
	slopetrees.append(trees)
print(slopetrees)
print(numpy.prod(slopetrees))
