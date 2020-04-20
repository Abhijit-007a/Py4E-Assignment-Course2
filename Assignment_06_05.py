str ="X-DSPAM-Confidence:  0.8475";
loc1 = str.find(" ")
loc2 = str.find("5")
num = str[loc1:loc2+1]
number = float(num.strip())
print (number)
