from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "This page should be login page and must include \"login\""

    def should_be_login_form(self):
        assert (self.is_element_present(*LoginPageLocators.LOGIN_EMAIL) and
                self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD) and
                self.is_element_present(*LoginPageLocators.LOGIN_BTN)), "Login form isn't presented"

    def should_be_register_form(self):
        assert (self.is_element_present(*LoginPageLocators.REG_EMAIL) and
                self.is_element_present(*LoginPageLocators.REG_PASSWORD) and
                self.is_element_present(*LoginPageLocators.REG_REPEAT_PAS) and
                self.is_element_present(*LoginPageLocators.REG_BTN)), "Registraton form isn't presented"

    def register_new_user(self, email, password):
        email_area = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        password_area = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        pass_repeat_area = self.browser.find_element(*LoginPageLocators.REG_REPEAT_PAS)
        email_area.send_keys(email)
        password_area.send_keys(password)
        pass_repeat_area.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        reg_btn.click()
