
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)

driver.implicitly_wait(3)     #wait for 5 seconds to perform the operation if the element is not found

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.LINK_TEXT, "Top Deals").click()

#driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

wait = WebDriverWait(driver,15)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//th[1]")))

driver.find_element(By.XPATH, "//th[1]").click()

browsersortedlist = []

elements = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
for element in elements:
  browsersortedlist.append(element.text)

copy = browsersortedlist.copy()

browsersortedlist.sort()

assert copy == browsersortedlist