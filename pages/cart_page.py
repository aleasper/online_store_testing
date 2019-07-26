from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_not_be_sth_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_FILLING), \
        "Basket should be empty"

    def should_be_text_empty_cart(self): # works only wiwth en-gb language
        text = self.browser.find_element(*CartPageLocators.BASKET_MESSAGE).text
        assert 'Your basket is empty' in text, \
        "Wrong emplty basket message: {}".format(text)
