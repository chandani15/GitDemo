#the setup fixture will be run before each method in class and yield will be run after each method of the class
#the cache fixture will be run once before class and yield will be run once after the class
#class name should always start with Test for pytest to identify it
#when the fixture does not return any data, we need not pass the ficture name as arg in the pytest methods
#here we did not pass setup and cache in the test cases in class

import pytest


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("cache")
class TestGroupFixture:
  
  def test_fixtureDemo1(self):
    print("I am in fixtureDemo1")

  def test_fixtureDemo2(self):
    print("I am in fixtureDemo2")

  def test_fixtureDemo3(self):
    print("I am in fixtureDemo3")
    