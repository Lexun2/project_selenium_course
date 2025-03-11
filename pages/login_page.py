from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):

    def register_new_user(self,email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT).click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "На странице логина форма логина is not present."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "На странице логина форма регистрации is not present."