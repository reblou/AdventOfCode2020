import re

class Passport:
	def process_tuples(self, ts):
		count = 0;
		for t in ts:
			k = t[0]
			if(k == "byr"):
				self.byr = t[1]
			elif (k == "iyr"):
				self.iyr = t[1]
			elif (k == "eyr"):
				self.eyr = t[1]
			elif (k == "hgt"):
				self.hgt = t[1]
			elif (k == "hcl"):
				self.hcl = t[1]
			elif (k == "ecl"):
				self.ecl = t[1]
			elif (k == "pid"):
				self.pid = t[1]
			elif (k == "cid"):
				self.cid = t[1]
			else:
				print("Error, incorrect key")
				continue
			count +=1
		self.total = count

	def is_valid(self):
		if (self.total == 8):
			print("8 full fields")
			return self.data_validation()
		elif(self.total == 7 and self.cid == -1):
			print("7 fields but only cid missing")
			return self.data_validation()
		else:
			print("Not enough fields, invalid")
			return False

	def data_validation(self):
		return self.byr_valid() and self.iyr_valid() and self.eyr_valid() and self.hgt_valid() and self.hcl_valid() and self.ecl_valid() and self.pid_valid()


	def byr_valid(self):
		ib = int(self.byr)
		return ib >= 1920 and ib <= 2002

	def iyr_valid(self):
		ii = int(self.iyr)
		return ii >= 2010 and ii <= 2020

	def eyr_valid(self):
		ie = int(self.eyr)
		return ie >= 2020 and ie <= 2030

	def hgt_valid(self):
		reg = "([0-9]+)(cm|in)"
		m = re.match(reg, self.hgt)
		if (m == None):
			return False
		ih = int(m[1])
		if (m[2] == "cm"):
			return ih >= 150 and ih <= 193
		elif(m[2] == "in"):
			return ih >= 59 and ih <= 76

	def hcl_valid(self):
		reg = "#[0-9a-f]{6}$"
		if re.search(reg, self.hcl):
			return True
		else:
			return False

	def ecl_valid(self):
		return self.colours.get(self.ecl)

	def pid_valid(self):
		reg = "^([0-9]{9})$"
		if (re.search(reg, self.pid)):
			return True
		else:
			return False

	def __init__(self, tuples):
		self.cid = -1
		self.process_tuples(tuples)
		self.colours = {
			"amb":1,
			"blu":1,
			"brn":1,
			"gry":1,
			"grn":1,
			"hzl":1,
			"oth":1
			}


file = open("4.txt", "r")
lines = file.readlines()


r = "(ecl|pid|eyr|hcl|byr|iyr|cid|hgt):(#?\w+)\s?"

passports = []
data = []
for l in lines:
	x = re.findall(r, l)
	print(x)
	if (len(x) > 0):
		data = data + x
	else:
		print("Data: ")
		print(data)
		passports.append(Passport(data))
		data = []

print("Last line Data: ")
print(data)
passports.append(Passport(data))


valid = 0
n = 0
for p in passports:
	print("Checking: " + str(n))
	if (p.is_valid()): 
		print("Is Valid")
		valid+=1
	n+=1
print("Total valid: " + str(valid))

