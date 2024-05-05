from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login:
    username_css = "#formEmail"
    otp_class = "pincode-input-text"
    button_login_xpath = "//button[contains(text(),'Sign In')]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, emailId):
        emailId_element = self.driver.find_element(By.CSS_SELECTOR, self.username_css)
        emailId_element.send_keys(emailId)

    def setPass(self, password):
        otp_place = self.driver.find_elements(By.CLASS_NAME, self.otp_class)
        for i in otp_place:
            i.send_keys(password)

    def clickLogin(self):
        retries = 3
        for _ in range(retries):
            try:
                wait = WebDriverWait(self.driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
                element.click()
                break
            except StaleElementReferenceException:
                continue
