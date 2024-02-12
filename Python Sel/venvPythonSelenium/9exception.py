itemsInCart = 0

#one way
#if itemsInCart != 2:
#  raise Exception("card count does not match")

#another way
#assert(itemsInCart == 2)

#try catch with error object e
try:
  with open('file.text','r') as reader:
    reader.read()
except Exception as e:
  print("in except")
  print(e)
finally:
  print("finally always gets executed whether try or except")