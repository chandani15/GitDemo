str = "Chandani.jain@gmail.com"
str2 = "QA Engineer"
str3 = "jain"

print(str[1])   #h (Iterate through each index)
print(str[0:8]) #Chandani (last index is exclusive)

print(str+" "+str2)   #Concat

print(str3 in str)    #True (substring validate )

splitting = str.split(".")
print(splitting[1])   #jain@gmail returns a list after splittling at seperator
print(splitting)

str4 = " Kothari "
print(str4.strip())   #trims both left and right spaces
print(str4.lstrip())
print(str4.rstrip())