import random
import time
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilites.locators import Locators

class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver, 10)
        self.driver = driver

    # Getters

    def get_you_city(self):
        return self.element_to_be_clickable((By.XPATH, Locators.YOU_CITY_ENTER))

    def get_all_category(self):
        return self.element_to_be_clickable((By.XPATH, Locators.all_category))

    def click_random_dropdown(self):
        """Выбираем случайную категорию товаров"""
        random_index = random.randint(1, 20) # Генерируем случайный локатор от 1 до 20
        random_locator = f'(//a[@class="dropdown-toggle"])[{random_index}]'
        category = self.element_to_be_clickable(random_locator)
        text_category = category.text
        print(f"Название категории: {text_category}")
        category.click()
        time.sleep(1)

    def main_page(self):
        self.get_you_city().click()
        time.sleep(2)
        self.get_all_category().click()
