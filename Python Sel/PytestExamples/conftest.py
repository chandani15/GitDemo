#defining the fixtures that can be used throughtout the folder
#if scope="class" then that ficture will be executed only once before class and yield in that will be executed only once after class

#use a arg "request" if the fixture has arg "params"
#use "request.param" to return 1 param at a time
#the test using the params fixture will run fomr each param in params
#we can pass multiple params in the single element in the list of params: see parameterize_multiple fixture


import pytest


@pytest.fixture()
def setup():
  print("I am setup")
  yield
  print("I am teardown")

@pytest.fixture(scope="class")
def cache():
  print("I am cache clearing start")
  yield
  print("I am cache clearing end")

@pytest.fixture()
def dataLoad():
  return ["Chandani", "Kothari", "chandani.jain@gmail.com"]

@pytest.fixture(params=["Chrome","Firefox","Edge"])
def parameterize(request):
  return request.param

@pytest.fixture(params=[("Chrome","Chandani","Kothari"), ("Firefox","Deepak"), "Edge"])
def parameterize_multiple(request):
  return request.param
  