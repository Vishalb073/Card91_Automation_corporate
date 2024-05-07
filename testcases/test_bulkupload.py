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
        file = "/home/vishal/Downloads/Corporate_Limits_updated1.csv"
        file1 = "/home/vishal/Downloads/Corporate_Limits_1 (7).csv"
        self.driver = login_setup1
        #self.driver.get(self.baseURL)
        self.bu = bulk_upload(self.driver)
        self.bu.bulk_btn()
        self.bu.file_download()
        self.bu.upload_btn(file)
        self.bu.customers()
        self.bu.upload_btn(file1)

