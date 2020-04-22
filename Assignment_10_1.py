senderlist = []
counts = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith("From "):
        linelist = line.split()
        sender = linelist[1]
        if sender in counts:
            counts[sender] = counts[sender] + 1
        else:
            counts[sender] =  1
                # More concise method of retrieving, creating, and updating
                # counts[sender] = counts.get(sender,0) + 1
    else:
        continue

# Using -1 as a flag in this case is acceptable because we are only dealing with
# positive values in finding the highest frequency email sender
largest = -1
prolific_sender = None
for key,value in counts.items():
    if value > largest:
        largest = value
        prolific_sender = key
print(prolific_sender, largest)
