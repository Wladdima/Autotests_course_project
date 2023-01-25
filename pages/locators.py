from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.btn-group > a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_REGISTRATION_FORM_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
   # "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    EMAIL_FIELD_REGISTRATION = (By.NAME, 'registration-email')
    PASSWORD_FIELD_REGISTRATION = (By.NAME, 'registration-password1')
    PASSWORD_AGAIN_FIELD_REGISTRATION = (By.NAME, 'registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    PRODUCT_PAGE_ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alertinner > strong')
    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner > p > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p')


class BasketPageLocators:
    BASKET_IS_EMPTY_LOCATOR = (By.CSS_SELECTOR, '#content_inner > p')
