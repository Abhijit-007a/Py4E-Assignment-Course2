senderlist = []
counts = dict()
fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

for line in fhand:
    if line.startswith("From "):
        linelist = line.split()
        sender = linelist[1]
        if sender in counts:
            counts[sender] = counts[sender] + 1
        else:
            counts[sender] =  1
    else:
        continue
largest = -1
big_sender = None
for key,value in counts.items():
    if value > largest:
        largest = value
        big_sender = key
print(big_sender, largest)
