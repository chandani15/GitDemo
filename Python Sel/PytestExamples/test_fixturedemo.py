#fixtures are used mostly for setup and teardown activities
#fixture will be executed first when the fixture function name is passed as arg to method
#the statements after yield will be executed after the method execution


import pytest

def test_NoRelationToFixture():
  print("I dont know about fixture")

@pytest.fixture()
def setup():
  print("I will be executing first")
  yield
  print("I will be executing last")

def test_FollowingSteps(setup):
  print("I am executing following steps")