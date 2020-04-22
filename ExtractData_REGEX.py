import re
fname = input("Enter the name of the file:")
fhand = open(fname)
count = 0
lines = fhand.read()
match = re.findall('[0-9]+',lines)
for i in match:
	number = int(i)
	count = count + number
print (count)
