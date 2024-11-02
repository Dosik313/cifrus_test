import time

from base.base_class import Base
from utilites.locators import Locators

class CartPageInput(Base):
    def __init__(self, driver, timeout):
        super().__init__(driver, 10)
        self.driver = driver


    def input_address_delivery(self):
        time.sleep(1)
        self.visibility_of_element_located(Locators.INPUT_CITY_DELIVERY)
        self.send_keys(Locators.INPUT_CITY_DELIVERY, f'Новосибирск, Новосибирская область, Россия')
        self.click_element(Locators.INPUT_CURRENT_CITY)
        time.sleep(2)
        self.send_keys(Locators.INPUT_ADDRESS_DELIVERY, f'{self.faker_smth().street_address()}')

    def input_details(self):
        random = len(self.find_elements(Locators.INPUT_DETAILS_CASHLESS))
        locator = f'{Locators.INPUT_DETAILS_CASHLESS}[{self.random_randint(1, random)}]'
        self.visibility_of_element_located(locator).click()
        self.window_info()
        self.send_keys(Locators.INPUT_ORGANIZATION_NAME, self.faker_smth().company())
        self.send_keys(Locators.INPUT_INN, self.faker_smth().individuals_inn())
        self.send_keys(Locators.INPUT_ENTITIES_ADDRESS, self.faker_smth().street_address())
        time.sleep(2)
