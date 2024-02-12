#read file into list
#reverse list
#wrire back the reversed list

#another way to open a file is as below, with this you need not do file.close() Python will do it afer the execution. Code optimization
file_path = "C:\\Users\\chand\\OneDrive\\Desktop\\Python Course\\Python Sel\\venvPythonSelenium\\test.txt" 
with open(file_path, 'r') as reader:
  lines = reader.readlines()
  reversed(lines)     #python has a function to directly reverse the list
  with open(file_path, 'w') as writer:
    for line in reversed(lines):
      writer.write(line) 
