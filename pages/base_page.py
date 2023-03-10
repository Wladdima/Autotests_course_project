from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from math import *


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)  # * - означает,
        # что передается пара элементов, которые надо распаковать
        login_link.click()

    def go_to_basket(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON_LOCATOR)
        basket_button.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"  # * - означает,
        # что передается пара элементов, которые надо распаковать

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'User is not authorized'

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_disappeared(self, how, what, timeout=4):  # если элемент исчезает, то возвращается True. Если, пока мы
        # ждем, элемент не исчезает (until not, то возвращаем False). Будет ждать пока элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))  # если элемент
            # за определенное время отображается, то возвращается False. Тест упадет, как только увидит искомый элемент
        except TimeoutException:
            return True
        return False
