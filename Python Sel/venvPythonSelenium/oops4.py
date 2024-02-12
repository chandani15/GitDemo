#__init__ is the construction in python
# access variables with self.
# class variables can be accessed by class name or the obj name

class Calculator():
  num = 100

  def __init__(self, c, d):
    print("in parent constructor")
    self.firstnumber = c
    self.secondnumber = d

  def getData(self):
    print("I am in getData")
    print(Calculator.num)
  
  def sum(self, a, b):
    print("in sum")
    return a + b + self.num

  def sub(self):
    print("in sub")
    return self.firstnumber - self.secondnumber

def outclass():
  obj = Calculator(2, 3)
  obj.getData()
  add = obj.sum(4, 5)
  print(add)

  obj1 = Calculator(6, 5)
  sub = obj1.sub()
  print(sub)

outclass()
