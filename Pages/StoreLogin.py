from selenium.webdriver.common.by import By

class StoreLoginPageLocators():
    NAME_INPUT = (By.ID, 'loginFrm_loginname')
    PASS_INPUT = (By.ID, 'loginFrm_password')
    LOGIN_BTN = (By.CSS_SELECTOR, '[title="Login"]')


class StoreLoginPage():

    def __init__(self, driver):
        self.driver = driver
    
    def get_input_name(self):
        return self.driver.find_element(*StoreLoginPageLocators.NAME_INPUT)

    def get_input_pass(self):
        return self.driver.find_element(*StoreLoginPageLocators.PASS_INPUT)
    
    def get_login_btn(self):
        return self.driver.find_element(*StoreLoginPageLocators.LOGIN_BTN)