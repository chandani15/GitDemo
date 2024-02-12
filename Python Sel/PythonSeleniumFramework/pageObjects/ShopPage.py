import sys
from selenium.webdriver.common.by import By

sys.path.append(r'C:\Users\chand\OneDrive\Desktop\Python Course\Python Sel\PythonSeleniumFramework')
from pageObjects.CheckoutPage import CheckOut

class ShopPage:
  shop = (By.LINK_TEXT, "Shop")
  
  def __init__(self, driver):
    self.driver = driver
  
  def shop_click(self):
    self.driver.find_element(*ShopPage.shop).click()
    checkout = CheckOut(self.driver)
    return checkout
    #return self.driver.find_element(*ShopPage.shop)
    #self.driver.find_element(By.LINK_TEXT, "Shop")