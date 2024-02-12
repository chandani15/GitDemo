
#driver.window_handles()
#driver.switch_to.window(handle)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

currentwindowhandles = driver.window_handles

driver.find_element(By.CLASS_NAME, "blinkingText").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.new_window_is_opened(currentwindowhandles))

windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
text = driver.find_element(By.XPATH, "//p[@class='im-para red']").get_attribute("textContent")
if text is not None:
  str_list = text.split(" ")

email = str_list[4]
print(f'email: {email}')

driver.close()

driver.switch_to.window(windowsOpened[0])

driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

