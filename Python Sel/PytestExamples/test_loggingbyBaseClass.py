#initialize the logger object in the BaseClassLog. Inherit the class here
#the log statments will also be printed in the html report. try with pytest --html=report.html -s. this command will run all the pytest in the folder.
#with this command you cannot se the print statement in report.html, but for this test case you can see the log statements.


from BaseClassLog import BaseClassLog


class TestDataPass(BaseClassLog):
  def test_getData(self, dataLoad):
    log = self.getLogger()
    log.info(dataLoad)
    log.warning(dataLoad[1])
    print(dataLoad)
    print(dataLoad[0])
    print(dataLoad[2])