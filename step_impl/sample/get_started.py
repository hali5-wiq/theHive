import os
from getgauge.python import before_suite, after_suite, step
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromeService
from uuid import uuid1
from getgauge.python import custom_screenshot_writer

class Driver:
    instance = None

@before_suite
def init():
    global browser
    #The following step actually start up the browser. Need a check here to indicate if API only or not. Then we can just run API.
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@after_suite
def close():
    browser.close()

@step("Search for <query>")
def go_to_get_started_page(query):
  textbox = browser.find_element(By.XPATH, "//textarea[@title = 'Search']")
  textbox.send_keys(query)
  textbox.send_keys(Keys.RETURN)

@step("Go to Google homepage at <url>")
def go_to_gauge_homepage_at(url):
    browser.get(url)

# Return a screenshot file name
@custom_screenshot_writer
def take_screenshot():
    image = browser.get_screenshot_as_png()
    file_name = os.path.join(os.getenv("gauge_screenshots_dir"), "screenshot-{0}.png".format(uuid1().int))
    file = open(file_name, "wb")
    file.write(image)
    return os.path.basename(file_name)
