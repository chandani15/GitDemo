#cascading of xpaths.
#waits
#implicit waits will not work on find elements returning a list. as list[] can be returned
#explicit wait: wait = WebDriverWait(driver, 10)
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)

driver.implicitly_wait(3)     #wait for 5 seconds to perform the operation if the element is not found

product_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)           #here implicite wait will not work as find_elements will return a null list and that is valid.
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
c = len(results)
assert c > 0
name_list = []
for result in results:
  name = result.find_element(By.XPATH, "h4").text
  name_list.append(name)
  result.find_element(By.XPATH, "div/button").click()         #dont put '/' when chaining xpaths
  

assert product_list == name_list

#buttons = driver.find_elements(By.XPATH, "//button[.='ADD TO CART']")      #directly selecting to add to cart
#for button in buttons:
#  button.click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[.='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[.='Apply']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)      #here implicit wait will work but it will wait only for 2 sec. for script to wait 10 sec use the explicit wait just for this statement

#code for sum of total and validate with total
elements = driver.find_elements(By.XPATH, "//tbody/tr/td[5]/p")
total = 0
for element in elements:
  price = element.text
  total = total + int(price)
print(f'total of products: {total}')

total_amt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(f'total amount: {total_amt}')

assert total_amt == total

total_after_dis = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
print(f'total after discount: {total_after_dis}')

assert total_after_dis < total_amt


