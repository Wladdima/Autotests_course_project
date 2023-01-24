import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time


@pytest.mark.parametrize('promo_offer_number', ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.
                                                                                  xfail(reason="bug")), '8', '9'])
class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser, promo_offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer_number}'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_the_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_see_new_book_in_basket()
        product_page.should_see_product_price()
        product_page.should_see_total_price_message()
        product_page.prices_should_be_equal()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, promo_offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer_number}'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_the_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_not_see_success_message()

    def test_guest_cant_see_success_message(self, browser, promo_offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer_number}'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_see_success_message()

    def test_guest_can_go_to_login_page_from_product_page(self, browser, promo_offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer_number}'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()

    def test_guest_cant_see_products_in_basket_opened_from_product_page(self, browser, promo_offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer_number}'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_basket()
        basket_page = BasketPage(browser, link)
        time.sleep(3)
        basket_page.should_be_empty()

    def test_guest_should_see_login_link_on_product_page(self, browser, promo_offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer_number}'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    def test_message_disappeared_after_adding_product_to_basket(self, browser, promo_offer_number):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer_number}'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_the_basket()
        product_page.solve_quiz_and_get_code()
        product_page.success_message_should_be_disappeared()
