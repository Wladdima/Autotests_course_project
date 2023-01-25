from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == LoginPageLocators.LOGIN_REGISTRATION_FORM_LINK, 'Login URL is not presented'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD_REGISTRATION)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_REGISTRATION)
        password_field.send_keys(password)
        password_again_field = self.browser.find_element(*LoginPageLocators.PASSWORD_AGAIN_FIELD_REGISTRATION)
        password_again_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        registration_button.click()
