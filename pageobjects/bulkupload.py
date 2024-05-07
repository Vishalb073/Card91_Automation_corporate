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
    dropdown_css = "css-8mmkcg"
    corporate_customers = "div.css-1nmdiq5-menu"
    file_upload = "button[class='sc-uVWWZ KeIfD btn btn-primary']"
    send_file = "input[class='sc-hCPjZK hcSoGo form-control']"
    upload = "button>div[class='sc-iGgWBj kqfRFm']"

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

    def upload_btn(self , file):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.file_upload).click()
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, self.send_file).send_keys(file)
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, self.upload).click()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="bulkupload",
                          attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def customers(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.dropdown_css).click()
            self.driver.find_element(By.CSS_SELECTOR, self.corporate_customers).click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    def upload_(self):
        try:
            self.driver.find_element(By.XPATH, self.upload).click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

    # def corporate_costoms(self):
    #     try:
    #         self.driver.find_element(By.CSS_SELECTOR, self.corporate_costoms)
    #     except NoSuchElementException as e:
    #         print(f"Element not found: {e}")
