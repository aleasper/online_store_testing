from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link) # initialization Page Object of main page
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

    new_page = LoginPage(page.browser, browser.current_url)
    new_page.should_be_login_page()
    #new_page.should_be_login_url()
    #new_page.should_be_login_form()
    #new_page.should_be_register_form()
