import time

from faker import Faker

from pages.order_page import OrderPage
from utilites.locators import Locators


class CartPage(OrderPage):
    def __init__(self, driver, title_item, price_item):
        super().__init__(driver)
        self.driver = driver
        self.title_item_in_cart = title_item
        self.price_item_in_cart = price_item



    def check_items_in_cart(self):
        time.sleep(2)
        title_item = self.get_text(Locators.TITLE_ITEM_IN_CART)
        print(f"Название товара в корзине: {title_item}")
        self.assert_value(self.title_item_in_cart, title_item)

        price_item = self.get_text(Locators.PRICE_ITEM_IN_CART)
        print(f"Цена товара в корзине: {price_item}")
        final_price_item = price_item.replace('Цена: ', '').replace(' руб.', '').strip()
        self.assert_value(final_price_item, price_item)

        price_all_item_in_cart = self.get_text(Locators.PRICE_ALL_ITEMS_IN_CART).replace(' руб.', '').replace(' ', '')
        delivery_price = self.get_text(Locators.DELIVERY_PRICE)
        sum_price = self.sum_values(price_all_item_in_cart, delivery_price)
        print(f"Общая сумма с доставкой: {sum_price}")
        total_price = int(self.get_text(Locators.TOTAL_PRICE).replace(' ', ''))
        self.assert_value(sum_price, total_price)

    def input_user_info(self):
        faker = Faker()
        elements = self.find_elements(Locators.INPUT_USER_INFO)
        for element in elements:
            self.action_chains().move_to_element(element).perform()
            print(f"enter locator")
            time.sleep(2)
            self.find_element(element).send_keys(faker.first_name())
            time.sleep(2)
            # self.send_keys(element, self.faker_smth().first_name())
            # print(f"ввел имя")

        time.sleep(3)
