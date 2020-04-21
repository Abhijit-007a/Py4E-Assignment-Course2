fname = input("Enter file name: ")
fhand = open(fname)
lst = list()
for line in fhand:
    for i in line.split():
        if not i in lst:
            lst.append(i)
lst.sort()
print (lst)
