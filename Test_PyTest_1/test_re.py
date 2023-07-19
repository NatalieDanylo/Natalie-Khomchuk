import re
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


def test_mytest5():
    driver = webdriver.Chrome(service=Service("C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe"),
                              options=options)
    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='signinEmail']"))).send_keys(    "Fusionbreak6@hillel.com")

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id^='signinPassword']"))).send_keys("Na131415")

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add car')]")))

    #txt = "Instructions"
    #x = re.findall("Instructions", txt)
    #print(x)
    #txt = "Hillel auto developed in Hillel IT school for educational purposes of QA courses"
    #x1 = re.search("^Hillel.*courses$", txt)
    #print(x1)
    #txt = "Add car"
    #x3 = re.search("Add car", txt)
    #print(x3)
    #txt = "Garage"
    #x4 = re.findall("Garage", txt)
    #print(x4)
    assert "Add car" in driver.page_source
    print(" Add car is present")
    value = ("Instructions")
    assert re.match("\w+", value)
    print("Instruction is a word and I am stubborn and have one more try")


    driver.close()
