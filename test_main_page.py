from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" # main page of online store
    page = MainPage(browser, link) # initialization Page Object of main page
    page.open()
    page.go_to_login_page()
