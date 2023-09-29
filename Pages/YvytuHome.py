from selenium.webdriver.common.by import By

class YvytuPageLocators():
    MAIN_TITLE = (By.CSS_SELECTOR, 'h1')


class YvytuPage():

    def __init__(self, driver):
        self.driver = driver

    def get_main_title(self):
        return self.driver.find_element(*YvytuPageLocators.MAIN_TITLE)