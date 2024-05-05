import pytest
import time
from selenium import webdriver
from pageobjects.loginpage import Login
from utilities.readProperties import ReadConfig

@pytest.fixture(scope="class")
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
