file = open("1.txt", "r")
afile = list(file)

for f in afile:
	i = int(f)
	search = str(2020-i) + "\n"
	print(str(i) + " looking for " + search)

	try:
		afile.index(search)
		print("Found: " + search + str(i))
		ans = int(search) * i
		print("++Answer++ " + str(ans))
		break

	except ValueError:
		print("For " + str(i) + " not found.")



