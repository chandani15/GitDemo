#find_elements() returns list of match elements. eg. all the li's in DOM

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("can")
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")
print(countries)
print(countries[1])
for country in countries:
  if country.text == "Canada":
    country.click()
    print("inside if")
    break

selected_country = driver.find_element(By.ID, "autosuggest").get_attribute("value")
assert "Canada" in selected_country # type: ignore
