import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class corporatePage:
    corporateBtn_xpath = "//span[contains(text(),'Corporate')]"
    onboardBtn_css = ".btn.btn-primary.my-2.btn-icon-text.btn.btn-primary"
    companyname_css = "#companyName"
    buisnesssType_css = "#companyDescription"
    cam_css = ".fe.fe-camera"
    file_css = "input[type='file']"
    Gst_num_Id = "gst"
    pan_num_Id = "pan"
    dropdown_Name = "css-8mmkcg"
    select_security = "div.css-1nmdiq5-menu"
    security_number_ID = "securityNumber"
    security_amount_ID = "securityAmount"
    address_css_path = "#addressOne"
    address_css_path2 = "#addressTwo"
    city_Id = "city"
    state_Id = "state"
    pincode_Id = "pincode"
    admin_name_Id = "adminName"
    admin_mobile_Id = "adminMobile"
    admin_email_Id = "adminEmail"
    submit_css = "//button[@id='corporateOnboardingForm']"
    closebtn_css = "btn-close"
    cardmap_xpath = "div>button>svg[viewBox='0 0 24 24']"
    submit_class = "div[class='sc-eqUAAy hIDAJQ']"
    def __init__(self, driver):
        self.driver = driver

    def corporate_button(self):
        retries = 3
        for _ in range(retries):
            try:
                wait = WebDriverWait(self.driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, self.corporateBtn_xpath)))
                element.click()
                break
            except StaleElementReferenceException:
                allure.attach(self.driver.get_screenshot_as_png(),name="testCorporate", attachment_type=AttachmentType.PNG)
                continue
        # self.driver.find_element(By.XPATH, self.corporateBtn_xpath).click()

    def onboard_button(self):
        try:
         self.driver.find_element(By.CSS_SELECTOR, self.onboardBtn_css).click()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def company_name(self, c_name):
        try:
            company_info = self.driver.find_element(By.CSS_SELECTOR, self.companyname_css)
            company_info.send_keys(c_name)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")
    def buisness_Type(self, buisness_Type):
        try:
            buisness = self.driver.find_element(By.CSS_SELECTOR, self.buisnesssType_css)
            buisness.send_keys(buisness_Type)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def company_logo(self, path):

        cam_option = self.driver.find_element(By.CSS_SELECTOR, self.cam_css)
        cam_option.click()

        self.driver.find_element(By.CSS_SELECTOR, self.file_css).send_keys(path)

    def gst_num(self, gstnumber):
        try:
            gst = self.driver.find_element(By.ID, self.Gst_num_Id)
            gst.send_keys(gstnumber)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def pan_num(self, pannumber):
        try:
            pan = self.driver.find_element(By.ID, self.pan_num_Id)
            pan.send_keys(pannumber)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def dropDown(self):
        try:
            dd = self.driver.find_element(By.CLASS_NAME, self.dropdown_Name)
            dd.click()
            self.driver.find_element(By.CSS_SELECTOR, self.select_security).click()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")
    # def dropDown(self):
    #     dd = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.CLASS_NAME, ))
    #     )
    #     dd.click()
    #     self.driver.find_element(By.CSS_SELECTOR, self.select_security).click()
    def security_num(self, securitynumber):
        try:
            number = self.driver.find_element(By.ID, self.security_number_ID)
            number.send_keys(securitynumber)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def security_amount(self, securityamount):
        try:
            amount = self.driver.find_element(By.ID, self.security_amount_ID)
            amount.send_keys(securityamount)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def address(self, address1):

        try:
            addr = self.driver.find_element(By.CSS_SELECTOR, self.address_css_path)
            addr.send_keys(address1)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def address_1(self, address2):
        try:
            addr1 = self.driver.find_element(By.CSS_SELECTOR, self.address_css_path2)
            addr1.send_keys(address2)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def addr_city(self, cities):
        try:
            city = self.driver.find_element(By.ID, self.city_Id)
            city.send_keys(cities)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def addr_state(self, state):
        try:
            states = self.driver.find_element(By.ID, self.state_Id)
            states.send_keys(state)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def addr_pin(self, pincode):
        try:
            pin = self.driver.find_element(By.ID, self.pincode_Id)
            pin.send_keys(pincode)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def admin_name(self, name):
        try:
            a_name = self.driver.find_element(By.ID, self.admin_name_Id)
            a_name.send_keys(name)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def admin_mobile(self, mobile):
        try:
            a_mobile = self.driver.find_element(By.ID, self.admin_mobile_Id)
            a_mobile.send_keys(mobile)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def admin_email(self, email):
        try:
            a_email = self.driver.find_element(By.ID, self.admin_email_Id)
            a_email.send_keys(email)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def submit_button(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            button = wait.until(EC.element_to_be_clickable((By.XPATH, self.submit_css)))
            button.click()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")
        # button = self.driver.find_element(By.XPATH, self.submit_css)
        # button.click()

    def close_button(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.closebtn_css).click()
            self.driver.refresh()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def card_map(self):

        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR , self.cardmap_xpath)
            print(len(elements))
            elements[0].click()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")

    def submit1(self):
        try:

            self.driver.find_element(By.CSS_SELECTOR , self.submit_class).click()
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="testCorporate", attachment_type=AttachmentType.PNG)
            print(f"Element not found: {e}")