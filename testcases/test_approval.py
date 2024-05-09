import time

from pageobjects import bulkupload
from pageobjects.approval_q import approval
from pageobjects.loginpage import Login
from testcases.conftest import login_setup1

from testcases.randomData import randomData
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
class TestApproval:
    baseURL = ReadConfig.geturl()

    @pytest.mark.usefixtures("login_setup1")
    def test_approval(self, login_setup1):
        self.driver = login_setup1
        self.aq = approval(self.driver)
        self.aq.approval_queue()

    def test_able_to_odd_box(self , login_setup1):
        self.LogGen.info("******* Starting Test_002_DDT_Login Test **********")
        self.driver = login_setup1
        self.aq = approval(self.driver)
        self.aq.approval_queue()
        self.aq.click_odd_checkBoxes()
        time.sleep(5)
        assert self.aq.check_odd_checkboxes_is_selected()

        # else:
        #     assert False


        time.sleep(2)

    def test_able_to_click_even_box(self , login_setup1):
        self.driver = login_setup1
        self.aq = approval(self.driver)
        self.aq.approval_queue()
        # self.aq.click_even_checkBoxes()
        assert self.aq.check_even_checkboxes_is_selected()

    def test_able_to_approve(self , login_setup1):
        self.driver = login_setup1
        self.aq = approval(self.driver)
        self.aq.approval_queue()
        self.aq.clickaccept(2)

    def test_aprovebutton_is_clicked(self , login_setup1):
        self.driver = login_setup1
        self.aq = approval(self.driver)
        self.aq.approval_queue()
        self.aq.check_clicked_ele(2)

    def test_status_of_customer(self , login_setup1):
        self.driver = login_setup1
        self.aq = approval(self.driver)
        self.aq.approval_queue()
