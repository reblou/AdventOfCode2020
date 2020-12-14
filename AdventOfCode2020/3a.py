file = open("3.txt", "r")
lines = file.readlines()

right = 3
down = 1

x = 0
trees = 0
i = 0

for l in lines:
	trulen = len(l) -1
	if i == 0 : 
		i += 1
		continue
		
	i += 1
	if (x+right >= trulen):
		print("overflow from " + str(x) + " on line " + str(i))
		new = x + right - trulen
		print("new pos: " + str(new))
		x = new
	else:
		x+=right

	land = l[x]
	print(land)
	if land == "#":
		trees += 1


print("Total trees: " + str(trees))
