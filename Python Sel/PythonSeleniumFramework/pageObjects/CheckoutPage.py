import sys
from selenium.webdriver.common.by import By

sys.path.append(r'C:\Users\chand\OneDrive\Desktop\Python Course\Python Sel\PythonSeleniumFramework')
from pageObjects.CartPage import Cart

class CheckOut:
  app_card = (By.XPATH, "//app-card")
  product_name = (By.XPATH, "div//h4/a")
  product_button = (By.XPATH, "div//button")
  checkout_button = (By.XPATH, "//a[contains(.,'Checkout')]")
  
  def __init__(self, driver):
    self.driver = driver

  def AppCard(self):
    return self.driver.find_elements(*CheckOut.app_card)
    #elements = self.driver.find_elements(By.XPATH, "//app-card")  
  
  def ProductName(self, element):
    return element.find_element(*CheckOut.product_name)
    #element.find_element(By.XPATH, "div//h4/a").text
  
  def ProductButton(self, element):
    return element.find_element(*CheckOut.product_button)
    #element.find_element(By.XPATH, "div//button").click()
  
  def CheckoutButton(self):
    self.driver.find_element(*CheckOut.checkout_button).click()
    cartpage = Cart(self.driver)
    return cartpage
    #return self.driver.find_element(*CheckOut.checkout_button)
    #self.driver.find_element(By.XPATH, "//a[contains(.,'Checkout')]").click()