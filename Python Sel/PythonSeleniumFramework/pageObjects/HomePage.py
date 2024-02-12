from selenium.webdriver.common.by import By

class HomePage:
  name = (By.NAME, "name")
  email = (By.NAME, "email")
  password = (By.ID, "exampleInputPassword1")
  checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
  gender = (By.ID, "exampleFormControlSelect1")
  status = (By.XPATH, "//input[@id='inlineRadio2']")
  dob = (By.NAME, "bday")
  submit = (By.XPATH, "//input[@type='submit']")
  success = (By.CLASS_NAME, "alert-success")
  
  def __init__(self, driver):
    self.driver = driver
  
  def input_name(self):
    return self.driver.find_element(*HomePage.name)
    #self.driver.find_element(By.NAME, "name").send_keys("Chandani")
    
  def input_email(self):
    return self.driver.find_element(*HomePage.email)
    #self.driver.find_element(By.NAME, "email").send_keys("chandani.jain@gmail.com")
  
  def input_password(self):
    return self.driver.find_element(*HomePage.password)
    #self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
  
  def check_icecream(self):
    return self.driver.find_element(*HomePage.checkbox)
    #self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
  
  def select_gender(self):
    return self.driver.find_element(*HomePage.gender)
    #elf.driver.find_element(By.ID, "exampleFormControlSelect1")
  
  def click_status(self):
    return self.driver.find_element(*HomePage.status)
    #self.driver.find_element(By.XPATH, "//input[@id='inlineRadio2']").click()
  
  def input_dob(self):
    return self.driver.find_element(*HomePage.dob)
    #self.driver.find_element(By.NAME, "bday").send_keys(1989-10-15)
    
  def click_submit(self):
    return self.driver.find_element(*HomePage.submit)
    #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    
  def scrape_success(self):
    return self.driver.find_element(*HomePage.success)
    #self.driver.find_element(By.CLASS_NAME, "alert-success").text
