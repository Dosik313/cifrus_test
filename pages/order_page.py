import random
import time
from base.base_class import Base
from utilites.locators import Locators


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver, 10)
        self.random_index_value = None
        self.title_item = None
        self.price_item = None

    def random_number(self):
        """Получаем случайный локатор от 1 до максимума на странице"""
        all_locators = len(self.driver.find_elements(Locators.all_name_locators))
        print(f"Всего локаторов {all_locators}")
        self.random_index_value = random.randint(1, all_locators)  # Выбираем случайный индекс
        print(f"Выбранный локатор: {self.random_index_value}")
        return self.random_index_value

    def get_title_item(self):
        name_locator = f'{Locators.name_item}[{self.random_index_value}]'
        element = self.find_element(name_locator)
        self.action_chains().move_to_element(element).perform()
        title_item = self.element_to_be_clickable(name_locator)
        self.title_item = title_item.text
        print(f"Вы выбрали товар с названием: {self.title_item}")
        return self.title_item

    def get_price_item(self):
        price_locator = f'{Locators.price_item}[{self.random_index_value}]'
        element = self.find_element(price_locator)
        self.action_chains().move_to_element(element).perform()
        price_item = self.element_to_be_clickable(price_locator)
        self.price_item = price_item.text
        print(f"Вы выбрали товар: {self.title_item}, его цена {self.price_item}")
        return self.price_item

    def click_add_co_cart(self):
        add_to_cart_locator = f'{Locators.add_to_cart_item}[{self.random_index_value}]'
        time.sleep(1)
        element = self.find_element(add_to_cart_locator)
        self.action_chains().move_to_element(element).perform()
        self.element_to_be_clickable((By.XPATH, add_to_cart_locator)).click()

    def check_items_before_cart(self):
        """Проверяем перед заходом в корзину цену и название"""
        title_item = self.get_text(Locators.check_title_before_cart)
        print(f"Проверка названия товара: {self.title_item}")
        self.assert_value(title_item,self.title_item)

        price_item = self.get_text(Locators.check_price_before_cart)
        final_price_item = price_item.replace('Цена: ', '').replace(' руб.', '').strip()
        print(f"Проверка цены товара: {final_price_item}")

        price_item_stored_cleaned = self.price_item.replace('Цена: ', '').replace(' руб.', '').strip()
        self.assert_value(final_price_item, price_item_stored_cleaned)

    def enter_to_cart(self):
        self.click_element(By.XPATH, Locators.ENTER_CART_BUTTON)
        text = self.get_text(Locators.CART_PAGE_TITLE)
        self.assert_value(value_1=text, value_2='Моя корзина')