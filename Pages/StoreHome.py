from selenium.webdriver.common.by import By

class StorePageLocators():
    ICON_FACEBOOK = (By.CSS_SELECTOR, '[title="Facebook"]')




class StorePage():

    def __init__(self, driver):
        self.driver = driver
    
    def get_facebook_icon(self):
        return self.driver.find_element(*StorePageLocators.ICON_FACEBOOK)
    
    def get_header_btn(self, txt):
        return self.driver.find_element(By.XPATH, "//a[contains(text(), '"+txt+"')]")