import time

from faker import Faker
from selenium.webdriver.common.by import By

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

        commissionn_price = self.get_text(Locators.COMMISSION)

        delivery_price = self.get_text(Locators.DELIVERY_PRICE)

        sum_price = self.sum_values(value_1=price_all_item_in_cart, value_2=commissionn_price, value_3=delivery_price)
        total_price = int(self.get_text(Locators.TOTAL_PRICE).replace(' ', ''))
        print(f"Общая сумма с доставкой: {sum_price}")
        print(f"Финальная сумма: {total_price}")
        self.assert_value(sum_price, total_price)

    def input_user_info(self):
        print(f"Ввожу значения в поля инпута юзера")
        # element = self.find_element(Locators.INPUT_USER_INFO)
        self.send_keys(Locators.INPUT_NAME_USER, self.faker_smth().first_name())
        self.send_keys(Locators.INPUT_EMAIL_USER, self.faker_smth().email())
        phone_number = self.faker_smth().numerify("+7 999" + "#######")
        self.send_keys(Locators.INPUT_NUMBER_USER, phone_number)
        self.move_to_element(find_locator=Locators.INPUT_NUMBER_USER)
        time.sleep(3)

    def delivery_method(self):
        while True:
            try:
                click_locator = f'{Locators.INPUT_DELIVERY_METHOD}[{self.generate_random_index(1,7)}]'
                print(click_locator)
                self.element_to_be_clickable((By.XPATH, click_locator)).click()
                time.sleep(2)
                if self.element_to_be_clickable((By.XPATH, Locators.QR_WINDOW_INFO)):
                    self.click_element(By.XPATH, Locators.QR_WINDOW_INFO)
            except Exception as e:
                print(f"Не нашел способ доставки {e}. Пробуем снова...")

        # for element in elements:
        #     self.action_chains().move_to_element(element).perform()
        #     print(f"enter locator")
        #     time.sleep(2)
        #     element.send_keys(self.faker_smth().first_name())
        #     print(f"ввел имя")
        #     element.send_keys(self.faker_smth().email())
        #     time.sleep(2)
        #     element.send_keys(self.faker_smth().phone_number())
        #     time.sleep(2)

            # self.send_keys(element, self.faker_smth().first_name())
            # print(f"ввел имя")

        time.sleep(3)
