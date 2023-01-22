from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_the_basket(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_ADD_TO_BASKET_BUTTON)
        add_product_button.click()

    def should_see_new_book_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LOCATOR).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text
        assert product_name_in_message == product_name, 'Product name in message is not equal to product name'

    def should_see_total_price_message(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE_MESSAGE), \
            'There is no total basket price message'

    def should_see_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), 'There is no product price'

    def prices_should_be_equal(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE_MESSAGE).text
        assert product_price == basket_total_price, 'Price in message is not equal to product price'
