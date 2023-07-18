from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--no-sandbox")
def test_mytest1():


    driver = webdriver.Chrome(service=Service("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe"), options=options)

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Guest log in')]"))).click()
    print("Guest log in button present")
    assert "Log out" in driver.page_source
    print("Log out present")
    driver.close()
