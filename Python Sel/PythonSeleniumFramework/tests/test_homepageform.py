from turtle import home
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import sys
sys.path.append(r'C:\Users\chand\OneDrive\Desktop\Python Course\Python Sel\PythonSeleniumFramework')
from  testData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestHomePageForm(BaseClass):
  driver : WebDriver
  def test_homepage(self, getData):
    logger = self.get_logger()
    homepage = HomePage(self.driver)
    homepage.input_name().send_keys(getData["first_name"])
    homepage.input_email().send_keys(getData["email"])
    homepage.input_password().send_keys(getData["password"])
    homepage.check_icecream().click()
    self.select_by_index(homepage.select_gender(), getData["gender_index"])
    #gender = Select(homepage.select_gender())
    #gender.select_by_index(1)
    homepage.click_status().click()
    homepage.input_dob().send_keys("1989-10-15")
    homepage.click_submit().click()
    message = homepage.scrape_success().text
    '''
    self.driver.find_element(By.NAME, "name").send_keys("Chandani")
    self.driver.find_element(By.NAME, "email").send_keys("chandani.jain@gmail.com")
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
    self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
    dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
    dropdown.select_by_index(1)
    self.driver.find_element(By.XPATH, "//input[@id='inlineRadio2']").click()
    self.driver.find_element(By.NAME, "bday").send_keys(1989-10-15)
    self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
    '''
    print(f"{getData['first_name']} : {message}")
    logger.info(f"{getData['first_name']} : {message}")
    assert "Success" in message
    self.driver.refresh()
  
  #@pytest.fixture(params=[("Chandani","chadani.jain@gmail.com","12345","1"),("Deepak","deepak@gmail.com","7890","0")])
  #@pytest.fixture(params=[{"first_name":"Chandani","email":"chandani.jain@gmail.com","password":"12345","gender_index":"1"},{"first_name":"Deepak","email":"deepak@gmail.com","password":"7890","gender_index":"0"}])
  @pytest.fixture(params=HomePageData.get_data("TC2"))
  def getData(self, request):
    return request.param
    
    
    