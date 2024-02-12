import sys
from selenium.webdriver.common.by import By

sys.path.append(r'C:\Users\chand\OneDrive\Desktop\Python Course\Python Sel\PythonSeleniumFramework')
from pageObjects.ConfirmPage import Confirm

class Cart:
  
  cart_products = (By.CSS_SELECTOR, ".media-body")
  product_name = (By.CSS_SELECTOR, "h4 a")
  checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
  
  def __init__(self, driver):
    self.driver = driver
  
  def CartProducts(self):
    return self.driver.find_elements(*Cart.cart_products)
    #self.driver.find_elements(By.CSS_SELECTOR, ".media-body")
  
  def ProductName(self, element):
    return element.find_element(*Cart.product_name)
    #ele.find_element(By.CSS_SELECTOR, "h4 a").text  

  def ClickCheckout(self):
    self.driver.find_element(*Cart.checkout_button).click()
    confirm = Confirm(self.driver)
    return confirm
    #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
  