from selenium.webdriver.common.by import By

class StoreAccountPageLocators():
    TITLE = (By.CSS_SELECTOR, 'h1')


class StoreAccountPage():

    def __init__(self, driver):
        self.driver = driver
    
    def get_main_title(self):
        return self.driver.find_element(*StoreAccountPageLocators.TITLE)