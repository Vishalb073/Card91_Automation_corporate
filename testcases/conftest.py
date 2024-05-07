import pytest
import time
from selenium import webdriver
from pageobjects.loginpage import Login
from utilities.readProperties import ReadConfig
from testcases.randomData import randomData

@pytest.fixture(scope='class')
def login_setup():
    baseURL = ReadConfig.getApplicationURL()
    emailId = ReadConfig.getusermail()
    password = ReadConfig.getuserpassword()

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(baseURL)
    lp = Login(driver)
    lp.setEmail(emailId)
    lp.setPass(password)
    lp.clickLogin()
    time.sleep(5)
    driver.refresh()

    yield driver
    driver.close()

@pytest.fixture(scope='class')
def login_setup1():
    baseUri = ReadConfig.geturl()
    phone_nu = ReadConfig.getph()
    password = ReadConfig.getuserpassword()

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(baseUri)

    lp = Login(driver)
    lp.setEmail(phone_nu)
    lp.setPass(password)
    lp.clickLogin()

# WebDriverWait(driver, 10).until(EC.url_to_be(baseUri))

    yield driver
    driver.close()
