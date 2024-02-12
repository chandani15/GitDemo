from selenium.webdriver.common.by import By

class Confirm:
  country = (By.ID, "country")
  
  def __init__(self, driver):
    self.driver = driver
  
  def Country(self):
    return self.driver.find_element(*Confirm.country)  
    #self.driver.find_element(By.ID, "country").send_keys("In")