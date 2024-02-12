#driver.switch_to.frame(id or name of frame)
#driver.switch_to.default_content()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, 'tinymce').clear()
driver.find_element(By.ID, 'tinymce').send_keys("Automation")

driver.switch_to.default_content()

assert "iFrame" in driver.find_element(By.TAG_NAME, "h3").text