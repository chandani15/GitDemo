#execute_script: to execute javascript
#get_screenshot_as_file: to take screenshot
#webdriver.ChromeOptions()
#chrome_options.add_argument("headless")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors--")

service_obj = Service()
driver = webdriver.Chrome(service= service_obj, options= chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scroll(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot1.png")