import csv
import os
import allure
import pytest
from selenium import webdriver

import testcases
import  time
from pageobjects.corporate import corporatePage

from testcases.randomData import randomData
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


@allure.severity(allure.severity_level.NORMAL)
class Test_corporate:
    baseURL = ReadConfig.getApplicationURL()
    emailId = ReadConfig.getusermail()
    password = ReadConfig.getuserpassword()
    company = ReadConfig.getComapny_name()
    buisness = ReadConfig.getBuisnesstype()
    logo = ReadConfig.getlogo()
    sec_num = ReadConfig.getsecuritynum()
    sec_amt = ReadConfig.getsecurityamount()
    address = ReadConfig.getaddress()
    address1 = ReadConfig.getaddress2()
    city = ReadConfig.getcity()
    state = ReadConfig.getstate()
    pin = ReadConfig.getpin()
    admin = ReadConfig.getadmin()
    phone = randomData.phone_nu

    # path = "testData/data.xlsx"

    def test_corporate(self, login_setup):
        self.driver = login_setup
        self.driver.get(self.baseURL)
        self.cp = corporatePage(self.driver)
        self.random_d = randomData()
        self.gst_no = self.random_d.generate_random_string()
        self.pan_nu = self.random_d.generate_random_Pan()
        # self.phone = self.random_d.genrate_random_phone()
        self.email = self.random_d.random_email()


        # self.rows = XLUtils.getRowCount(self.path, 'sheet1')
        #
        # for r in range(2, self.rows + 1):
        #     self.company = XLUtils.readData(self.path, 'sheet1', r, 1)
        #     self.buisness = XLUtils.readData(self.path, 'sheet1', r, 2)
        #     self.logo = XLUtils.readData(self.path, 'sheet1', r, 3)
        #     self.sec_Num = XLUtils.readData(self.path, 'sheet1', r, 4)
        #     self.sec_amt = XLUtils.readData(self.path, 'sheet1', r, 5)
        #     self.address = XLUtils.readData(self.path, 'sheet1', r, 6)
        #     self.address1 = XLUtils.readData(self.path, 'sheet1', r, 7)
        #     self.city = XLUtils.readData(self.path, 'sheet1', r, 8)
        #     self.state = XLUtils.readData(self.path, 'sheet1', r, 9)
        #     self.pin = XLUtils.readData(self.path, 'sheet1', r, 10)
        #     self.adminname = XLUtils.readData(self.path, 'sheet1', r, 11)
        #
        #
        self.cp.corporate_button()
        self.cp.onboard_button()
        self.cp.company_name(self.company)
        self.cp.buisness_Type(self.buisness)
        self.cp.company_logo(self.logo)
        self.cp.gst_num(self.gst_no)
        self.cp.pan_num(self.pan_nu)
        self.cp.approval_limit(1000000)
        self.cp.dropDown()
        self.cp.security_num(self.sec_num)
        self.cp.security_amount(self.sec_amt)
        self.cp.address(self.address)
        self.cp.address_1(self.address1)
        self.cp.addr_city(self.city)
        self.cp.addr_state(self.state)
        self.cp.addr_pin(self.pin)
        self.cp.admin_name(self.admin)
        self.cp.admin_mobile(self.phone)
        self.cp.admin_email(self.email)
        self.cp.submit_button()
        time.sleep(10)
        # self.cp.close_button()

        # time.sleep(5)
        # self.cp.card_map()
        # time.sleep(5)
        # self.cp.dropDown()
        # self.cp.submit1()
