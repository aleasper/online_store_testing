from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.main_page import MainPage
import pytest
import random

def get_random_email_pass(): # utility function
    random.seed()
    fake_email = 'fake{}@fmail.com'.format(str(int(random.random()*100000)))
    fake_pass = 'ilovestepik'
    return (fake_email, fake_pass)

@pytest.mark.register_user
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link) # initialization Page Object of main page
        page.open()
        page.go_to_login_page()

        new_page = LoginPage(page.browser, browser.current_url)
        new_page.register_new_user(*get_random_email_pass())
        new_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review # for review on Stepik
    def test_user_can_add_product_to_cart(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_btn()
        page.add_item_to_basket()
        #page.solve_quiz_and_get_code()
        page.should_item_in_basket()

@pytest.mark.need_review # for review on Stepik
def test_guest_can_add_product_to_cart(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_item_to_basket()
    #page.solve_quiz_and_get_code()
    page.should_item_in_basket()

@pytest.mark.need_review # for review on Stepik
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()

    new_page = CartPage(page.browser, browser.current_url)
    new_page.should_not_be_sth_in_cart()
    new_page.should_be_text_empty_cart() # works only with en-gb language

@pytest.mark.need_review # for review on Stepik
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.guest_positive
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

'''
list_of_page_params = a = [x for x in range(10)]

@pytest.mark.parametrize('page_param', list_of_page_params)
def test_guest_can_add_product_to_cart_promo(browser, page_param):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(page_param)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_item_in_basket()
'''

@pytest.mark.guest_negative
def test_guest_cant_see_success_message(self, browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
