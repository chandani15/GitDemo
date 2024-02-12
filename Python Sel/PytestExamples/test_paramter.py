#define a fixture in conftest
#this test there runs 3 times (i.e. for each param defined in the parameterize fixture)


def test_params(parameterize):
  print(parameterize)
  
def test_params_multiple(parameterize_multiple):
  print(parameterize_multiple[1])