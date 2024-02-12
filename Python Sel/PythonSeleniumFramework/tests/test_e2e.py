from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

import sys

sys.path.append(r'C:\Users\chand\OneDrive\Desktop\Python Course\Python Sel\PythonSeleniumFramework')
from pageObjects.ShopPage import ShopPage
from pageObjects.CheckoutPage import CheckOut
from pageObjects.CartPage import Cart
from pageObjects.ConfirmPage import Confirm
from utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures("setup_browser")
class TestDemo(BaseClass):
  driver : WebDriver
  
  def test_e2e(self):
    products = ["Samsung Note 8", "Nokia Edge"]
    logger = self.get_logger()
    shoppage = ShopPage(self.driver)
    checkout = shoppage.shop_click()
    #shoppage.shop_click().click()
    #self.driver.find_element(By.LINK_TEXT, "Shop").click()
    
    logger.info("clicked on shop link")

    #checkout = CheckOut(self.driver)
    elements = checkout.AppCard()
    #elements = self.driver.find_elements(By.XPATH, "//app-card") 
    found = 0 
    for element in elements:
      name = checkout.ProductName(element).text
      #name = element.find_element(By.XPATH, "div//h4/a").text
      if name in products:
        checkout.ProductButton(element).click()
        #element.find_element(By.XPATH, "div//button").click()
        found += 1
    
    if found != len(products):
      logger.error("Product/Products were not found in card")
    else:
      logger.info("All Products added to cart")

    cartpage = checkout.CheckoutButton()
    #self.driver.find_element(By.XPATH, "//a[contains(.,'Checkout')]").click()

    cart = []
    #cartpage = Cart(self.driver)
    elements = cartpage.CartProducts()
    #elements = self.driver.find_elements(By.CSS_SELECTOR, ".media-body")
    for ele in elements:
      cart.append(cartpage.ProductName(ele).text)
      #cart.append(ele.find_element(By.CSS_SELECTOR, "h4 a").text)
      
    assert cart == products

    confirm = cartpage.ClickCheckout()
    #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    
    confirm.Country().send_keys("In")
    #self.driver.find_element(By.ID, "country").send_keys("In")
    
    self.visibility_of_element("suggestions")
    #wait = WebDriverWait(self.driver, 15)
    #wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "suggestions")))

    countries = self.driver.find_elements(By.CSS_SELECTOR, "div[class=suggestions] ul")
    for country in countries:
      country_name = country.find_element(By.XPATH, "li/a").text
      print(country_name)
      if country_name == "India":
        country.find_element(By.XPATH, "li/a").click()
        logger.info("Selected country name India")
        break
  
    self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
    self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

    message = self.driver.find_element(By.XPATH, "//div[contains(@class,'alert')]").text
    print(message)
    if "Success!" in message:
      logger.info(message)
    else:
      logger.error("the test not successful. Success is not in "+message)
    assert "Success!" in message
