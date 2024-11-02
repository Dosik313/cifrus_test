import time

from pages.order_page import OrderPage
from utilites.locators import Locators
from pages.cart_page_input import CartPageInput


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
        commission_price = self.get_text(Locators.COMMISSION).replace(' ', '')
        delivery_price = self.get_text(Locators.DELIVERY_PRICE)

        sum_price = self.sum_values(value_1=price_all_item_in_cart, value_2=commission_price, value_3=delivery_price)
        total_price = int(self.get_text(Locators.TOTAL_PRICE).replace(' ', ''))
        print(f"Общая сумма с доставкой: {sum_price}")
        print(f"Финальная сумма: {total_price}")
        self.assert_value(sum_price, total_price)

    def input_user_info(self):
        self.send_keys(Locators.INPUT_NAME_USER, self.faker_smth().first_name())
        self.send_keys(Locators.INPUT_EMAIL_USER, self.faker_smth().email())
        phone_number = self.faker_smth().numerify("+7 999" + "#######")
        self.send_keys(Locators.INPUT_NUMBER_USER, phone_number)
        self.move_to_element(find_locator=Locators.INPUT_NUMBER_USER)

    def delivery_method(self):
        if self.find_element(Locators.INPUT_DELIVERY_CDEK):
            self.click_element(locator=Locators.INPUT_DELIVERY_CDEK)
            check_address_str = self.get_text(Locators.ADDRESS_CHECK)
            self.assert_value(check_address_str, 'Адрес')
            CartPageInput(self.driver, 10).input_address_delivery()
        else:
            element = self.visibility_of_element_located(Locators.TEXT_PICKUP_ORDER)
            if element:
                element.click()
                text_pickup = self.get_text(Locators.TEXT_PICKUP_ORDER)
                self.assert_value(text_pickup, 'самовывоз (ул. 2-я Филёвская, 15/19)')
                self.click_element(Locators.INPUT_CASH_PAYMENT)
                text_cash_payment = self.get_text(Locators.TEXT_CHECK_CASH_PAYMENT)
                self.assert_value(text_cash_payment, 'Инструкция для оплаты Наличными')

    def payment_method(self):
        check_locators = len(self.find_elements(Locators.INPUT_PAYMENT_METHOD))
        current_locator = self.random_randint(1, check_locators)
        locator_payment = f'{Locators.INPUT_PAYMENT_METHOD}[{current_locator}]'
        if check_locators == 1:
            self.click_element(locator_payment)
            self.move_to_element(Locators.TEXT_BANK_PAYMENT)
            text_bank_payment = self.get_text(Locators.TEXT_BANK_PAYMENT)
            self.assert_value(text_bank_payment, 'Инструкция для оплаты Дебетовой картой через Сбербанк Онлайн (комиссия 3%)')
        elif check_locators == 2:
            self.click_element(locator_payment)
            self.move_to_element(Locators.TEXT_QR_PAYMENT)
            check_qr_payment = self.get_text(Locators.TEXT_QR_PAYMENT)
            self.assert_value(check_qr_payment, 'Инструкция для оплаты Банковской картой по Системе быстрых платежей по QR (комиссия 5%)')
        else:
            self.click_element(locator_payment)
            check_legal_entities = self.get_text(Locators.TEXT_LEGAL_ENTITIES)
            self.assert_value(check_legal_entities, 'Реквизиты')
            self.window_info()
            CartPageInput(self.driver, 10).input_details()

    def click_confirm_button(self):
        self.move_to_element(Locators.CONFIRM_BUTTON)
        self.click_element(Locators.CONFIRM_BUTTON)
        time.sleep(3)
