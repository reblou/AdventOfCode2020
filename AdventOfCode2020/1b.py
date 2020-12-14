class Double:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.val = a+b

file = open("1.txt", "r")

doubles = []

lines = file.readlines()
for i in range(0, len(lines)):
	n = int(lines[i])

	for ib in range(0, len(lines)):
		if (i != ib):
			m = int(lines[ib])
			if ((n+m) <= 2020):
				doubles.append(Double(n, m))

		
for l in lines:
	ln = int(l)
	sval = 2020-ln

	for d in doubles:
		if d.val == sval:
			print(str(ln) + " " + str(d.a) + " " + str(d.b))
			print("++Ans++ " + str(ln*d.a*d.b))
			raise SystemExit(0)


