from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import driver
from base.base_class import Base



class TestBuy:
    def test_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.main_page()
        main_page.click_random_dropdown()

        order_page = OrderPage(driver)
        order_page.random_number()
        order_page.random_title_item()
        order_page.random_price_item()
        order_page.click_add_co_cart()
        order_page.check_items_before_cart()
        order_page.enter_to_cart()

        cart_page = CartPage(driver, order_page.title_item, order_page.price_item)
        cart_page.check_items_in_cart()
        cart_page.input_user_info()


    # def test_order_page(self,driver):
    #     order_page = OrderPage(driver)
    #     order_page.random_number()
    #     order_page.random_title_item()
    #     order_page.random_price_item()
    #     order_page.click_add_co_cart()
    #     order_page.check_items_before_cart()
    #     order_page.enter_to_cart()

