#dataLoad is a fixture defined in conftest.py
#when we are returning the data from a fixture we need to pass the fixture name as arg to pytest method
#here was passed dataLoad in the pytest test case
#the class name should start with Test
#the function name should start with _test



class TestDataPass():
  def test_getData(self, dataLoad):
    print(dataLoad)
    print(dataLoad[0])
    print(dataLoad[2])
