import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time


@pytest.mark.parametrize('address', ['promo=offer0', 'promo=offer1', 'promo=offer2', 'promo=offer3', 'promo=offer4',
                                     'promo=offer5', 'promo=offer6', pytest.param('promo=offer7', marks=pytest.mark.
                                                                                  xfail(reason="bug")), 'promo=offer8',
                                     'promo=offer9'])
def test_guest_can_add_product_to_basket(browser, address):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{address}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_the_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_see_new_book_in_basket()
    product_page.should_see_product_price()
    product_page.should_see_total_price_message()
    product_page.prices_should_be_equal()
#    time.sleep(120)


@pytest.mark.parametrize('address', ['promo=offer0', 'promo=offer1', 'promo=offer2', 'promo=offer3', 'promo=offer4',
                                     'promo=offer5', 'promo=offer6', pytest.param('promo=offer7', marks=pytest.mark.
                                                                                  xfail(reason="bug")), 'promo=offer8',
                                     'promo=offer9'])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, address):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{address}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_the_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_see_success_message()


@pytest.mark.parametrize('address', ['promo=offer0', 'promo=offer1', 'promo=offer2', 'promo=offer3', 'promo=offer4',
                                     'promo=offer5', 'promo=offer6', pytest.param('promo=offer7', marks=pytest.mark.
                                                                                  xfail(reason="bug")), 'promo=offer8',
                                     'promo=offer9'])
def test_guest_cant_see_success_message(browser, address):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{address}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_see_success_message()


@pytest.mark.parametrize('address', ['promo=offer0', 'promo=offer1', 'promo=offer2', 'promo=offer3', 'promo=offer4',
                                     'promo=offer5', 'promo=offer6', pytest.param('promo=offer7', marks=pytest.mark.
                                                                                  xfail(reason="bug")), 'promo=offer8',
                                     'promo=offer9'])
def test_message_disappeared_after_adding_product_to_basket(browser, address):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{address}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_the_basket()
    product_page.solve_quiz_and_get_code()
    product_page.success_message_should_be_disappeared()
