from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service()
driver = webdriver.Chrome(service= service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
driver.maximize_window()

products = ["Samsung Note 8", "Nokia Edge"]

driver.find_element(By.LINK_TEXT, "Shop").click()

elements = driver.find_elements(By.XPATH, "//app-card")
for element in elements:
  name = element.find_element(By.XPATH, "div//h4/a").text
  if name in products:
    element.find_element(By.XPATH, "div//button").click()

driver.find_element(By.XPATH, "//a[contains(.,'Checkout')]").click()

cart = []
elements = driver.find_elements(By.CSS_SELECTOR, ".media-body")
for ele in elements:
  cart.append(ele.find_element(By.CSS_SELECTOR, "h4 a").text)
  
assert cart == products

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("In")
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "suggestions")))

countries = driver.find_elements(By.CSS_SELECTOR, "div[class=suggestions] ul")
for country in countries:
  country_name = country.find_element(By.XPATH, "li/a").text
  print(country_name)
  if country_name == "India":
    country.find_element(By.XPATH, "li/a").click()
    break

driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

message = driver.find_element(By.XPATH, "//div[contains(@class,'alert')]").text
print(message)
assert "Success!" in message
