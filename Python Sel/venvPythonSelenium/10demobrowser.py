from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://about.google/?fg=1&utm_source=google-CA&utm_medium=referral&utm_campaign=hp-header")    #click on about
print(driver.title)
driver.minimize_window()
driver.maximize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()