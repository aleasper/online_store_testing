from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def testtest_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link) # initialization Page Object of main page
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link) # initialization Page Object of main page
        page.open()
        page.go_to_login_page()

        new_page = LoginPage(page.browser, browser.current_url)
        new_page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link) # initialization Page Object of main page
    page.open()
    page.go_to_basket_page()

    new_page = CartPage(page.browser, browser.current_url)
    new_page.should_not_be_sth_in_cart()
    new_page.should_be_text_empty_cart() # works only wiwth en-gb language

    '''
    import random
    random.seed()
    fake_email = 'fake{}@fmail.com'.format(str(int(random.random()*1000)))
    '''
