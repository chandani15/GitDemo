from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Chandani"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alertBox = driver.switch_to.alert
alertText = alertBox.text
print(alertText)
assert name in alertText
alertBox.accept()       #clicks on OK in javacript/browser alert boxes
#alertBox.dismiss()     #clicks on cancel in javascript/browser alert boxes
