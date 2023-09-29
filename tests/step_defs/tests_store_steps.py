from pytest_bdd import scenarios, when, then, parsers
from Pages.StoreHome import StorePage
from Pages.StoreLogin import StoreLoginPage
from Pages.StoreAccount import StoreAccountPage
import time

#Scenario
scenarios('../features/Store.feature')

@when(parsers.parse('hace click en el icono de "{icon}"'))
def click_main_icon(browser, icon):
    store_page = StorePage(browser)
    store_page.get_facebook_icon().click()

@then(parsers.parse('se redirecciona a "{web_url}"'))
def check_url_another_tab(browser, web_url):
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(6)
    assert web_url in browser.current_url

@when(parsers.parse('presiona el boton "{btn}" del header'))
def click_header_button(browser, btn):
    store_page = StorePage(browser)
    store_page.get_header_btn(btn).click()
    time.sleep(6)

@when('completa usuario, password y presiona el boton de Login')
def login_user(browser):
    store_login = StoreLoginPage(browser)
    store_login.get_input_name().send_keys("agusDarwoft")
    store_login.get_input_pass().send_keys("automation")
    store_login.get_login_btn().click()

@then(parsers.parse('se verifica que el titulo es "{titulo}"'))
def verify_main_title(browser, titulo):
    store_account = StoreAccountPage(browser)
    assert titulo in store_account.get_main_title().text