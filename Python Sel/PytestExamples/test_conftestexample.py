#this will look for setup fixture first in local and then in conftest execute that and then execute the method and then yield if any

def test_fixtureDemo1(setup):
  print("I am in fixtureDemo1")

def test_fixtureDemo2(setup):
  print("I am in fixtureDemo2")

def test_fixtureDemo3(setup):
  print("I am in fixtureDemo3")