# pip install pytest, pytest --version
# Any pytest filename should start with or end with test_ or _test
#the file must contain only functions
#method names should start with test_
#methods should not have same name else they get overridden by the latest method of that name

#to run in terminal, do 
# 1. pytest file_name.py    #can also do py.test <filename.py>
# 2. pytest file_name.py -v (more info) 
# 3. pytest file_name.py -s (print statement)
# 4. run all the pytest in a folder: pytest -v -s
# 5. run only some tests: pytest -k CreditCard -v -s   #this will run all the tests in the PytsetExamples folder matching substring CreditCard
# 6. run with custom marks: on method defination: @pytest.mark.smoke, command to run: pytest -m smoke -v -s     #here smoke is custom
# 7. skip some methods from the entire folder run: @pytest.mark.skip, then give command pytest -v -s, the test_Greet() will be skipped
# 8. run the method but dont report as pass or fail: @pytest.mark.xfail
# 9. To generate HTML report: first install with cmd: pip install pytest-html. then run pytest --html=report.html. with this report.html file will be created

import pytest


@pytest.mark.smoke
def test_firstProgram():
  print("Hello")

@pytest.mark.skip
def test_Greet():
  print("Good morning")
  
def test_FirstCreditCard():
  print("In the first method of Credit Card")