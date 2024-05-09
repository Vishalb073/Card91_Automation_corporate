import csv

import allure
import pytest
from allure_commons.types import AttachmentType

from pageobjects.bulkupload import bulk_upload
from testcases.conftest import login_setup1
from testcases.errors import PAN_NUMBER_ERROR_MESSAGE, EMAIL_ID_ERROR_MESSAGE, AADHAR_NUMBER_ERROR_MESSAGE, \
    FIRSTNAME_ERROR_MESSAGE, LAST_NAME_ERROR_MESSAGE, MOBILE_NUMBER_ERROR_MESSAGE, DUPLICATE_DATA_ERROR_MESSAGE, \
    DESIGNATION_ERROR_MESSAGE, LEVEL_ERROR_MESSAGE, DEPARTMENT_ERROR_MESSAGE, CURR_SALARY_ERROR_MESSAGE, \
    EMPLOYEE_ERROR_MESSAGE, SECURITY_AMOUNT_ERROR_MESSAGE
import time
import datetime
import logging

from utilities.customlogger import LogGen


@allure.severity(allure.severity_level.NORMAL)
class Test_Bulkupload:

    logging.info("Testing started")

    logger = LogGen.logger()
    e_msg = [AADHAR_NUMBER_ERROR_MESSAGE, EMAIL_ID_ERROR_MESSAGE, PAN_NUMBER_ERROR_MESSAGE,
             FIRSTNAME_ERROR_MESSAGE, LAST_NAME_ERROR_MESSAGE, MOBILE_NUMBER_ERROR_MESSAGE,
             DUPLICATE_DATA_ERROR_MESSAGE, DESIGNATION_ERROR_MESSAGE, LEVEL_ERROR_MESSAGE,
             CURR_SALARY_ERROR_MESSAGE, DEPARTMENT_ERROR_MESSAGE, EMPLOYEE_ERROR_MESSAGE,
             SECURITY_AMOUNT_ERROR_MESSAGE]

    def upload_file_and_check_reason(self, filepath, e_msg, login_setup1):
        self.driver = login_setup1
        self.bu = bulk_upload(self.driver)
        self.logger.info("============logged in to corporate portal============")
        self.bu.bulk_btn()
        time.sleep(5)
        self.bu.customers()
        self.bu.customers_file(filepath)
        time.sleep(2)
        self.bu.upload_()
        time.sleep(2)

        self.bu.download()
        time.sleep(5)
        download_text = self.bu.download_text()
        time.sleep(2)
        file = "/home/vishal/Downloads/" + download_text
        retries = 3
        for _ in range(retries):
            self.logger.info("============getting downloaded file============")
            try:
                with open(file, 'r', encoding='utf-8') as data:
                    data_reader = csv.DictReader(data)
                    for reasons in data_reader:
                        reason = str(reasons['Reason'])

                        if reason in e_msg:
                            print(e_msg[e_msg.index(reason)])
                            assert reason == e_msg[e_msg.index(reason)]
                            self.logger.info("============csv data testcases passed============")
            except FileNotFoundError as e:
                allure.attach(self.driver.get_screenshot_as_png(), name="bulkupload",
                              attachment_type=AttachmentType.PNG)
                print(f"file not found: {e}")

    def test_reasons(self, login_setup1):
        file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload.csv"
        self.upload_file_and_check_reason(file1, self.e_msg, login_setup1)

    #
    # def test_email_id_error(self ,login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_Email.csv.csv"
    #     self.upload_file_and_check_reason(file1, EMAIL_ID_ERROR_MESSAGE, login_setup1)
    #
    # def test_pan_number_error(self ,login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_pan_nu.csv.csv"
    #     self.upload_file_and_check_reason(file1, PAN_NUMBER_ERROR_MESSAGE, login_setup1)
    #
    # @pytest.mark.order(1)
    # def  test_first_name_error(self , login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_firstname.csv"
    #     self.upload_file_and_check_reason(file1, FIRSTNAME_ERROR_MESSAGE, login_setup1)
    #
    # def test_last_name_error(self, login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_lastname.csv.csv"
    #     self.upload_file_and_check_reason(file1, LAST_NAME_ERROR_MESSAGE, login_setup1)
    #
    # def test_phone_number_error(self, login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_phone_nu.csv.csv"
    #     self.upload_file_and_check_reason(file1, MOBILE_NUMBER_ERROR_MESSAGE, login_setup1)
    #
    # def test_duplicate_data_error(self, login_setup1):
    #     file1 = "/home/vishal/Downloads/.csv"
    #     self.upload_file_and_check_reason(file1, DUPLICATE_DATA_ERROR_MESSAGE, login_setup1)
    #
    # def test_designation_error(self , login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_designation.csv"
    #     self.upload_file_and_check_reason(file1, DESIGNATION_ERROR_MESSAGE, login_setup1)
    #
    # def test_level_error(self, login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_level.csv.csv"
    #     self.upload_file_and_check_reason(file1, LEVEL_ERROR_MESSAGE, login_setup1)
    #
    # def test_curr_salary(self , login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_level.csv.csv"
    #     self.upload_file_and_check_reason(file1, CURR_SALARY_ERROR_MESSAGE, login_setup1)
    # def test_department_name(self , login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_level.csv.csv"
    #     self.upload_file_and_check_reason(file1, DEPARTMENT_ERROR_MESSAGE, login_setup1)
    # def test_emp_id_isvalid(self , login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_level.csv.csv"
    #     self.upload_file_and_check_reason(file1, EMPLOYEE_ERROR_MESSAGE, login_setup1)
    # # def test_security_number(self , login_setup1):
    # #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_level.csv.csv"
    # #     self.upload_file_and_check_reason(file1, SECURITY_AMOUNT_ERROR_MESSAGE, login_setup1)
    # def test_age_is_greater_than_eighteen(self , login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_level.csv.csv"
    #     self.upload_file_and_check_reason(file1, LEVEL_ERROR_MESSAGE, login_setup1)
    #
    # def test_security_amount(self , login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload_level.csv.csv"
    #     self.upload_file_and_check_reason(file1, SECURITY_AMOUNT_ERROR_MESSAGE, login_setup1)
    #
    # def test_file_upload(self, login_setup1):
    #     file1 = "/home/vishal/Downloads/Corporate Customers Bulk Upload.csv.csv"
    #     self.upload_file_and_check_reason(file1, "sucess", login_setup1)

    def test_uploaded_file_date(self, login_setup1):
        self.logger.info("============ Validating time ============")
        file_path = "/home/vishal/Downloads/Corporate Customers Bulk Upload.csv"
        self.driver = login_setup1
        self.bu = bulk_upload(self.driver)

        self.bu.bulk_btn()
        time.sleep(5)
        self.bu.customers()
        self.bu.customers_file(file_path)
        time.sleep(2)
        self.bu.upload_()
        time.sleep(2)
        date_str = self.bu.get_curr_date()

        date_obj = datetime.datetime.strptime(date_str, "%B %dth %Y").date()

        assert date_obj == datetime.datetime.now().date()

    def test_file_records_is_displayed(self, login_setup1):
        self.logger.info("============validating record numbers ============")
        file_path = "/home/vishal/Downloads/Corporate Customers Bulk Upload.csv"
        self.driver = login_setup1
        self.bu = bulk_upload(self.driver)

        self.bu.bulk_btn()
        time.sleep(5)
        self.bu.customers()
        self.bu.customers_file(file_path)
        time.sleep(2)
        self.bu.upload_()
        time.sleep(2)
        records = self.bu.filerecords()
        assert records.is_displayed()

    def test_failed_file_records_is_displayed(self, login_setup1):
        self.logger.info("============Validating failed records============")
        file_path = "/home/vishal/Downloads/Corporate Customers Bulk Upload.csv"
        self.driver = login_setup1
        self.bu = bulk_upload(self.driver)

        self.bu.bulk_btn()
        time.sleep(5)
        self.bu.customers()
        self.bu.customers_file(file_path)
        time.sleep(2)
        self.bu.upload_()
        time.sleep(2)

        records = self.bu.get_failedrecords()
        assert records.is_displayed()

    def test_sucess_file_record_is_displayed(self, login_setup1):
        self.logger.info("============Validating failed records============")
        file_path = "/home/vishal/Downloads/Corporate Customers Bulk Upload.csv"
        self.driver = login_setup1
        self.bu = bulk_upload(self.driver)

        self.bu.bulk_btn()
        time.sleep(5)
        self.bu.customers()
        self.bu.customers_file(file_path)
        time.sleep(2)
        self.bu.upload_()
        time.sleep(2)
        records = self.bu.get_sucessrecords()
        assert records.is_displayed()
