from .pages.product_page import ProductPage
import pytest

'''
def test_guest_can_add_product_to_cart(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_item_to_basket()
    #page.solve_quiz_and_get_code()
    page.should_item_in_basket()
'''

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

'''
def test_message_disappeared_after_adding_product_to_cart(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_item_to_basket()
    page.should_success_message_disappered()

'''