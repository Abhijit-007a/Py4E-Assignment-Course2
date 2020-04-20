fname = input("Enter the name of the file:")
fhand = open(fname)
for i in fhand :
        i=i.rstrip().upper()
        print(i)
        
