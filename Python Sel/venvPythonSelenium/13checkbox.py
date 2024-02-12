#get_attribute()  to get the attribute of an element 
#is_selected() to chcek if selected for radio button and checkbox
#is_displayed() to check if the element is displayed or not on screen
#is_enabled() to check enable or disable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
  if checkbox.get_attribute("value") == "option2":
    checkbox.click()
    assert checkbox.is_selected()
    print(checkbox.is_selected())
    break

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed()    #will fail here as hidden the textbox by the above click
