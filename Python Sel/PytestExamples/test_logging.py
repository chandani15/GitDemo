#import logging package and do getlogger(__name__) : here __name__ will help pass the py testcase name
#filehandler will create a log file
#formatter will help define the format of log line
#setFormatter will help pass the format information to filehandler
#addhandler will give info of file handler to logger
#levels are debug, info, warning, error, critical
#setlevel can help define what levels should be seen in the log. Eg. if its info, then debug will not be shown

import logging

def test_loggingDemo():
  logger = logging.getLogger(__name__)

  fileHandler = logging.FileHandler("logfile.log")
  formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
  fileHandler.setFormatter(formatter)

  logger.addHandler(fileHandler)

  logger.setLevel(logging.INFO)

  logger.debug("This is Debug")
  logger.info("This is Info")
  logger.warning("This is Warning")
  logger.error("This is Error")
  logger.critical("This is critical")