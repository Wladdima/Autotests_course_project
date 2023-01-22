from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_REGISTER_FORM_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class ProductPageLocators:
#    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
#    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    PRODUCT_PAGE_ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alertinner > strong')
    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner > p > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p')
