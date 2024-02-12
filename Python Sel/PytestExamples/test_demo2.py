
import pytest


@pytest.mark.smoke
def test_assert():
  msg = "I am demo 2"
  assert "1" in msg, "This is not demo 1"
  
@pytest.mark.xfail
def test_secondCreditCard():
  a = 4
  b = 6
  assert a+2 == b