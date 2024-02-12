from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from selenium.webdriver.edge.service import Service as ES
from selenium.webdriver.common.by import By
import pytest
driver : None

def pytest_addoption(parser):
  parser.addoption(
    "--browsername", action = "store", default = "chrome", help = "my option: chrome, firefox, IE "
  )
  parser.addoption(
    "--url", action = "store", default = "https://rahulshettyacademy.com/angularpractice/", help = "my option: https://rahulshettyacademy.com/angularpractice/"
  )
  parser.addoption(
    "--testcasename", action = "store", default = "https://rahulshettyacademy.com/angularpractice/", help = "my option: https://rahulshettyacademy.com/angularpractice/"
  )

@pytest.fixture()
def setup_browser(request):
  global driver
  browser = request.config.getoption("--browsername")
  url = request.config.getoption("--url")
  testcase = request.config.getoption("--testcasename")
  if browser == "chrome":
    service_obj = CS()
    driver = webdriver.Chrome(service= service_obj)
  elif browser == "firefox":
    service_obj = FS()
    driver = webdriver.Firefox(service= service_obj)
  elif browser == "IE":
    service_obj = ES()
    driver = webdriver.Edge(service= service_obj)

  #driver.get("https://rahulshettyacademy.com/angularpractice/")
  driver.get(url)
  driver.implicitly_wait(5)
  driver.maximize_window()
  request.cls.driver = driver
  request.cls.testcase = testcase
  yield
  driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                      'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
  driver.get_screenshot_as_file(name)