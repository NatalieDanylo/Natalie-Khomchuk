from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()

options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe"), options=options)


driver.get("https://www.browserstack.com/")

time.sleep(2) #sleep for 2 sec

assert "BrowserStack" in driver.title

goButton = driver.find_element(By.ID, "primary-menu")
goButton.click()

time.sleep(2) #sleep for 2 sec
assert "No results found." not in driver.page_source

driver.close()