import random
from imghdr import tests

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Base:

    def __init__(self, driver, timeout):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, element):
        return self.driver.find_element(By.XPATH, element)

    def find_elements(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    def faker_smth(self):
        faker = Faker('ru_RU')
        return faker

    def send_keys(self, locator, value):
        element = self.find_element(locator)
        if element:
            # Преобразуем значение в строку, если это необходимо
            element.send_keys(str(value))
        else:
            print(f"Элемент с локатором {locator} не найден.")

    def action_chains(self):
        return ActionChains(self.driver)

    def move_to_element(self,find_locator):
        element = self.find_element(find_locator)
        if element:
            self.action_chains().move_to_element(element).perform()
        else:
            print(f"Локатор: {find_locator} не найден")

    def generate_random_index(self, start_value, end_value):
        return random.randint(start_value, end_value)

    def visibility_of_element_located(self, selector, locator):
        return self.wait.until(EC.visibility_of_element_located((selector, locator)))

    def element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_text(self, locator):
        text = self.visibility_of_element_located(By.XPATH, locator).text
        return text

    def click_element(self, selector, locator):
        return self.visibility_of_element_located(selector, locator).click()

    def assert_value(self, value_1, value_2):
        assert value_1 == value_2, f"Ошибка валидации {value_1} : {value_2}"

    def sum_values(self,value_1,value_2, value_3):
        total = int(value_1) + int(value_2) + int(value_3)
        return total