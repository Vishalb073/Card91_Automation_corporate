from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
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
                continue
        # self.driver.find_element(By.XPATH, self.corporateBtn_xpath).click()

    def onboard_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.onboardBtn_css).click()

    def company_name(self, c_name):
        company_info = self.driver.find_element(By.CSS_SELECTOR, self.companyname_css)
        company_info.send_keys(c_name)

    def buisness_Type(self, buisness_Type):
        buisness = self.driver.find_element(By.CSS_SELECTOR, self.buisnesssType_css)
        buisness.send_keys(buisness_Type)

    def company_logo(self, path):
        cam_option = self.driver.find_element(By.CSS_SELECTOR, self.cam_css)
        cam_option.click()

        self.driver.find_element(By.CSS_SELECTOR, self.file_css).send_keys(path)

    def gst_num(self, gstnumber):
        gst = self.driver.find_element(By.ID, self.Gst_num_Id)
        gst.send_keys(gstnumber)

    def pan_num(self, pannumber):
        pan = self.driver.find_element(By.ID, self.pan_num_Id)
        pan.send_keys(pannumber)

    def dropDown(self):
        dd = self.driver.find_element(By.CLASS_NAME, self.dropdown_Name)
        dd.click()
        self.driver.find_element(By.CSS_SELECTOR, self.select_security).click()

    # def dropDown(self):
    #     dd = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.CLASS_NAME, "your_class_name_here"))
    #     )
    #     dd.click()
    #     self.driver.find_element(By.CSS_SELECTOR, self.select_security).click()
    def security_num(self, securitynumber):
        number = self.driver.find_element(By.ID, self.security_number_ID)
        number.send_keys(securitynumber)

    def security_amount(self, securityamount):
        amount = self.driver.find_element(By.ID, self.security_amount_ID)
        amount.send_keys(securityamount)

    def address(self, address1):
        addr = self.driver.find_element(By.CSS_SELECTOR, self.address_css_path)
        addr.send_keys(address1)

    def address_1(self, address2):
        addr1 = self.driver.find_element(By.CSS_SELECTOR, self.address_css_path2)
        addr1.send_keys(address2)

    def addr_city(self, cities):
        city = self.driver.find_element(By.ID, self.city_Id)
        city.send_keys(cities)

    def addr_state(self, state):
        states = self.driver.find_element(By.ID, self.state_Id)
        states.send_keys(state)

    def addr_pin(self, pincode):
        pin = self.driver.find_element(By.ID, self.pincode_Id)
        pin.send_keys(pincode)

    def admin_name(self, name):
        a_name = self.driver.find_element(By.ID, self.admin_name_Id)
        a_name.send_keys(name)

    def admin_mobile(self, mobile):
        a_mobile = self.driver.find_element(By.ID, self.admin_mobile_Id)
        a_mobile.send_keys(mobile)

    def admin_email(self, email):
        a_email = self.driver.find_element(By.ID, self.admin_email_Id)
        a_email.send_keys(email)

    def submit_button(self):
        # wait = WebDriverWait(self.driver, 10)  # Wait for a maximum of 10 seconds
        # button = wait.until(EC.element_to_be_clickable((By.XPATH, self.submit_css)))
        # button.click()
        button = self.driver.find_element(By.XPATH, self.submit_css)
        button.click()

