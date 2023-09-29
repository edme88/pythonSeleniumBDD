from pytest_bdd import scenarios, then, parsers
from Pages.YvytuHome import YvytuPage

# Scenarios
scenarios('../features/Yvytu.feature')

@then(parsers.parse('el titulo principal es "{main_title}"'))
def check_main_title(browser, main_title):
    yvytu_page = YvytuPage(browser)
    assert yvytu_page.get_main_title().text in main_title
    print('Se verifico el titulo: '+main_title)
