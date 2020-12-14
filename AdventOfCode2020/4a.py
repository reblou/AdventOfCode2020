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
			return False

	def data_validation(self):


		return True


	def __init__(self, tuples):
		self.cid = -1
		self.process_tuples(tuples)


file = open("4.txt", "r")
lines = file.readlines()


r = "(ecl|pid|eyr|hcl|byr|iyr|cid|hgt):(#?\w+)\s"

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
for p in passports:
	if (p.is_valid()): valid+=1

print("Total valid: " + str(valid))



