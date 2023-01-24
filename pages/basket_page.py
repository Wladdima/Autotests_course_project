from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
from .locators import BasePageLocators
from .locators import BasketPageLocators
from .base_page import BasePage
from math import *


class BasketPage(BasePage):

    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_LOCATOR), 'Basket is not empty'
