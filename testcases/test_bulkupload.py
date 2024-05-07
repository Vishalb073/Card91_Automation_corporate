from telnetlib import EC

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import testcases
import time
from pageobjects.bulkupload import bulk_upload
from pageobjects.loginpage import Login

from testcases.randomData import randomData
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
@allure.severity(allure.severity_level.NORMAL)
class TestBulkUpload:
    baseURL = ReadConfig.geturl()

    @pytest.mark.usefixtures("login_setup1")
    def test_bulk(self, login_setup1):
        file = "/home/vishal/Downloads/Corporate_Limits_updated4.csv"
        file1 = "/home/vishal/Downloads/Corporate_Limits_1 (8).csv"
        self.driver = login_setup1
        #self.driver.get(self.baseURL)
        self.bu = bulk_upload(self.driver)
        self.bu.bulk_btn()
        self.bu.file_download()
        self.bu.upload_btn()
        self.bu.send_key(file)
        time.sleep(2)
        self.bu.upload_()
        time.sleep(5)
        self.bu.customers()
        self.bu.customers_file(file1)
        # self.bu.upload_btn(file1)

