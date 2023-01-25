from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_LOCATOR), 'Basket is not empty'
