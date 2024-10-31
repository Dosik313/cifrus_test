import random
import time
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilites.locators import Locators


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver, 10)
        self.random_index_value = None
        self.title_item = None
        self.price_item = None

    def random_number(self):
        all_locators = self.driver.find_elements(By.XPATH, Locators.all_name_locators)
        print(f"Всего локаторов {len(all_locators)}")
        self.random_index_value = random.choice(range(len(all_locators)))  # Выбираем случайный индекс
        print(f"Выбранный локатор: {self.random_index_value}")
        return self.random_index_value

    def random_title_item(self):
        name_locator = f'{Locators.name_item}[{self.random_index_value}]'
        print(f"локатор названия товара {name_locator}")
        element = self.find_element(name_locator)
        self.action_chains().move_to_element(element).perform()
        title_item = self.element_to_be_clickable((By.XPATH, name_locator))
        self.title_item = title_item.text
        print(f"Вы выбрали товар с названием: {self.title_item}")
        return self.title_item

    def random_price_item(self):
        price_locator = f'{Locators.price_item}[{self.random_index_value}]'
        print(f"локатор цены товара: {price_locator}")
        element = self.find_element(price_locator)
        self.action_chains().move_to_element(element).perform()
        price_item = self.element_to_be_clickable((By.XPATH, price_locator))
        self.price_item = price_item.text
        print(f"Вы выбрали товар: {self.title_item}, его цена {self.price_item}")
        return self.price_item

    def click_add_co_cart(self):
        add_to_cart_locator = f'{Locators.add_to_cart_item}[{self.random_index_value}]'
        print(f"Локатор кнопки добавить: {add_to_cart_locator}")
        time.sleep(1)
        element = self.find_element(add_to_cart_locator)
        self.action_chains().move_to_element(element).perform()
        click_add_to_cart = self.element_to_be_clickable((By.XPATH, add_to_cart_locator))
        click_add_to_cart.click()

        time.sleep(2)

    def check_items_before_cart(self):
        """Проверяем перед заходом в корзину цену и название"""
        title_item = self.visibility_of_element_located(By.XPATH, Locators.check_title_before_cart).text
        print(f"Название товара после клика на кнопку 'В корзину': {self.title_item}")
        self.assert_value(title_item,self.title_item)
        print(f"Все четко")

        price_item = self.visibility_of_element_located(By.XPATH, Locators.check_price_before_cart).text
        final_price_item = price_item.replace('Цена: ', '').replace(' руб.', '').strip()
        print(f"цена товара: {final_price_item}")

        price_item_stored_cleaned = self.price_item.replace('Цена: ', '').replace(' руб.', '').strip()

        assert final_price_item == price_item_stored_cleaned, f"Ошибка валидации цены товара: {price_item}"
        print(f"Все четко")

    def enter_to_cart(self):
        self.click_element(By.XPATH, Locators.ENTER_CART_BUTTON)
        text = self.get_text(Locators.CART_PAGE_TITLE)
        self.assert_value(value_1=text, value_2='Моя корзина')
        print(f"все четко")