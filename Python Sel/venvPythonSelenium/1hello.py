'''
Datatypes in Python
Numeric (int,float,complex number)
String
List
Tuple
Dictionary
'''

msg = "hi"
print(msg)
a = 1 + 1
print (f"{msg} {a}")
print("{} {}".format(msg,a))

b, c, d = 3, 6.5, "bye"

print("{} {} {}".format(b,c,d))
print(f'{b} {c} {d}')

print(type(b))
print(type(c))
print(type(d))

#cannot concatenate with + two different types of variables. can concatenate with + two strings.
#print(c + d)     ERROR

print(msg + d)

#list
values = [1, 2, 3, "chandani", 4]
print(values[0])  #1
print(values[2])  #3
print(values[-1])  #4 the last element
print(values[1:3])  #2,3 the last index is excluded

values.insert(2, 2.5)
print(values)   #[1, 2, 2.5, 3, 'chandani', 4]  inserted a new 2nd index with value 2.5

values.append("End")
print(values)   #[1, 2, 2.5, 3, 'chandani', 4, 'End'] appened at the end the value End

values[4] = "CHANDANI"
print(values)   #[1, 2, 2.5, 3, 'CHANDANI', 4, 'End'] updates the 4th index

del values[0]
print(values)   #[2, 2.5, 3, 'CHANDANI', 4, 'End'] deletes the 1st index

#Tuple (same as list but immutable - cannot update a tuple)
tup = (1,2,3, "chandani", 5)
#tup[1] = "2.5"   not allowed


#Dictionary key:value pairs
dict = {1:"hi", "two":5, "name":"chandani", 6:10}
print(dict[1])
print(dict["name"])
print(dict[6])

#adding values to dic
dict["add"] = "adding"
print(dict)

dic = {}
dic["first_name"] = "chandani"
dic["last_name"] = "kothari"
dic["gender"] = "female"
print(dic)
print(dic["gender"])