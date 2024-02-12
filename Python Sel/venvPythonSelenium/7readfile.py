file_path = "C:\\Users\\chand\\OneDrive\\Desktop\\Python Course\\Python Sel\\venvPythonSelenium\\test.txt" 
#file_path = r"C:\Users\chand\OneDrive\Desktop\Python Course\Python Sel\venvPythonSelenium\test.txt"   #using raw string or in the path you can use \\
file = open(file_path)
#print(file.read())     #full file

#print(file.read(5))     #abc d, IMP: if file.read() is executed before this, then it does not print anything as the control has already reached the last line

#print(file.readline())  #reads one line.  efg - as the control is after d now
#print(file.readline())  #reads the next line. hijkl

#reading a full file with while loop and readline() function
'''
line = file.readline()
while line != "":
  print(line)
  line = file.readline()
'''

#readlines() - returns all the lines in a file as a list 
lines = file.readlines()
for line in lines:
  print(line)

file.close()