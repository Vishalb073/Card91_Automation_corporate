import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait




class bulk_upload:
    ccms_btn_xpath = '//a[@href="/bulkUpload/"]'
    file_download_xpath = "//a[@class ='d-flex tx-12 justify-content-start mt-1']"
    dropdown_css = "svg.css-8mmkcg"
    corporate_customers = "div.css-1nmdiq5-menu"
    #file_upload = "button[class='sc-uVWWZ KeIfD btn btn-primary']"
    file_upload = "//*[@id='__next']/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/button"
    # send_file = "input[class='sc-hCPjZK hcSoGo form-control']"
    send_file = "//*[@id='__next']/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/button/input"
    # file_upload = "button[class='sc-jxOSlx bphwTE btn btn-primary']"
    # upload = "button>div[class='sc-iGgWBj kqfRFm']"
    upload = "div>button[class='undefined position-relative btn btn-primary']"
    # upload = "//div[normalize-space() = 'Upload the file']"
    failed_download = "//*[@id='cell-9-undefined']"
    failed_text = "//*[@id='cell-9-undefined']/a"
    curr_date = "//*[@id='cell-3-undefined']/div/div"
    file_records = "//*[@id='cell-5-undefined']/div"
    failed_file_rec = "//*[@id='cell-7-undefined']/div"
    sucess_rec = "//*[@id='cell-6-undefined']/div"
    message_read = "//*[@id='13']/div[1]/div[2]/text()"

    def __init__(self, driver):
        self.driver = driver

    def bulk_btn(self):
        retries = 3
        for _ in range(retries):
            try:
                wait = WebDriverWait(self.driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, self.ccms_btn_xpath)))
                element.click()
                break
            except StaleElementReferenceException:
                allure.attach(self.driver.get_screenshot_as_png(), name="bulkupload",
                              attachment_type=AttachmentType.PNG)
                continue

    def file_download(self):
        try:
            self.driver.find_element(By.XPATH, self.file_download_xpath).click()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="bulkupload",
                          attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def upload_btn(self ):
        try:
            self.driver.find_element(By.XPATH, self.file_upload).click()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="bulkupload",
                          attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def send_key(self , file):
        self.driver.find_element(By.XPATH, self.send_file).send_keys(file)
        time.sleep(2)
        # self.driver.find_element(By.XPATH, self.upload).click()

    def customers(self ):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.dropdown_css).click()
            self.driver.find_element(By.CSS_SELECTOR, self.corporate_customers).click()
            time.sleep(2)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def customers_file(self , file1):
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.file_upload)))
        # element.click()
        try:
            self.driver.find_element(By.XPATH, self.file_upload).click()
            self.driver.find_element(By.XPATH, self.send_file).send_keys(file1)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def upload_(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.upload).click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")


    def download(self):
       try:
            webs = self.driver.find_element(By.XPATH , self.failed_download)
            webs.click()
       except NoSuchElementException as e:
           print(f"Element not found: {e}")


    def download_text(self):
        try:
            self.driver.implicitly_wait(10)
            webs = self.driver.find_element(By.XPATH,self.failed_text )
            f = webs.text
            return  f
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def filerecords(self):
        try:
            total_files = self.driver.find_element(By.XPATH, self.file_records)
            return total_files
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def get_failedrecords(self):
        try:
            failed_rec = self.driver.find_element(By.XPATH ,self.failed_file_rec )
            return failed_rec
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def get_sucessrecords(self):
        try:
            sucess_rec = self.driver.find_element(By.XPATH ,self.failed_file_rec )
            return sucess_rec
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def get_curr_date(self):
        try:
            c_date = self.driver.find_element(By.XPATH, self.curr_date)
            curr_day = c_date.text
            return  curr_day
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def get_sucess_message(self):
            alertwindow = self.driver.find_element(By.XPATH , "//div[@class='Toastify']//div//div//div//div[2]")
            alert_text =  alertwindow.text
            return alert_text


    # def get_message(self):
    #     mess = self.driver.find_element(By.XPATH , self.message_read)
    #     message = mess.text
    #     return message
    # # def corporate_costoms(self):
    #     try:
    #         self.driver.find_element(By.CSS_SELECTOR, self.corporate_costoms)
    #     except NoSuchElementException as e:
    #         print(f"Element not found: {e}")

