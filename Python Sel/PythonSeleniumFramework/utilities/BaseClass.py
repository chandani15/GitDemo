import logging
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup_browser")
class BaseClass:
  driver : WebDriver
  
  def visibility_of_element(self, text):
    wait = WebDriverWait(self.driver, 15)
    wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, text)))
  
  def select_by_index(self, locator, index):
    gender = Select(locator)
    gender.select_by_index(index)
    
  def get_logger(self):
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("LogFile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    return logger