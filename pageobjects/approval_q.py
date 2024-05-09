import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class approval:
    approval_btn_xpath = "//a[@href='/approvalQueue/']"
    all_check_box = "input[type = 'checkbox']"
    check_box_xpath = "//div[contains(@id,'cell-1')]/div/span/input"
    application_id_xpath = "//div[contains(@id,'cell-1')]/div/span/input"
    all_info_xpath = "//div[contains(@id,'cell-8-')]/div/i"
    status_xpath = "//div[contains(@id,'cell-7')]/span"
    rejct_btn_xpath = "//div[contains(@id,'cell-8')]/div/button[2]"
    accept_btn_xpath = "//div[contains(@id,'cell-8')]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def approval_queue(self):
        retries = 3
        for _ in range(retries):
            try:
                wait = WebDriverWait(self.driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, self.approval_btn_xpath)))
                element.click()
                break
            except StaleElementReferenceException:
                allure.attach(self.driver.get_screenshot_as_png(), name="approval_queue",
                              attachment_type=AttachmentType.PNG)
                continue

    def click_all_checkboxes(self):

        btns = self.driver.find_elements(By.CSS_SELECTOR, self.all_check_box)
        btns[0].click()


    def check_box_status(self):
        boxes = self.driver.find_elements(By.XPATH, self.all_check_box)
        boxes.is_selected()


    def click_odd_checkBoxes(self):
        elements = self.driver.find_elements(By.XPATH, self.check_box_xpath)
        for i, element in enumerate(elements):
         if i % 2 == 1 :  # Check odd index and not already selected
            element.click()

    def check_odd_checkboxes_is_selected(self):
        elements = self.driver.find_elements(By.XPATH, self.check_box_xpath)
        for i, element in enumerate(elements):
            if i % 2 == 1:  # Check odd index and not already selected
               return  element.is_selected()



    def click_even_checkBoxes(self):
        elements = self.driver.find_elements(By.XPATH, self.check_box_xpath)
        for i, element in enumerate(elements):
            if i % 2 == 0:
                element.click()

    def check_even_checkboxes_is_selected(self):
        elements = self.driver.find_elements(By.XPATH, self.check_box_xpath)
        for i, element in enumerate(elements):
            if i % 2 == 0:
                return element.is_displayed()


    def get_all_application_id(self):
        elements = self.driver.find_elements(By.XPATH, self.application_id_xpath)
        list_app = []

        for i in elements:
            list_app.append(i.text)

    def view_all_info(self):
        elements = self.driver.find_elements(By.XPATH, self.all_info_xpath)
        elements[0].click()

    def click_all_accept(self): #last
        elements = self.driver.find_elements(By.XPATH, self.accept_btn_xpath)
        for i, element in enumerate(elements):
                element.click()

    def click_odd_accept(self):
        elements = self.driver.find_elements(By.XPATH, self.all_check_box)
        for i, element in enumerate(elements):
            if i % 2 == 1:
                element.click()

    def click_even_accept(self):
        elements = self.driver.find_elements(By.XPATH, self.all_check_box)
        for i, element in enumerate(elements):
            if i % 2 == 0:
                element.click()


    def check_status(self):
        elements = self.driver.find_elements(By.XPATH, self.status_xpath)
        list_status =[]
        for i, element in enumerate(elements):
            list_status.append(element)


    def clickaccept(self , index):
        elements = self.driver.find_elements(By.XPATH, self.accept_btn_xpath)
        elements[index].click()

    def check_clicked_ele(self , index):
        elements = self.driver.find_elements(By.XPATH, self.accept_btn_xpath)
        elements[index].is_selected()








