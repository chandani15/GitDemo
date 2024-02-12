from oops4 import Calculator

class ChildImp(Calculator):
  num2 = 200

  def __init__(self):
    print("in child constructor")
    Calculator.__init__(self, 3, 2)

  def getCompleteData(self):
    print("in getCompleteData")
    return self.num2 + self.num
  
  def getCompleteSub(self):
    print("in getCompleteSub")
    return self.num2 - self.num - self.sub()

child = ChildImp()
print(child.getCompleteData())
print(child.getCompleteSub())
