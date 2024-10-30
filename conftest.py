import time

import pytest
from selenium import webdriver

base_url = 'https://www.cifrus.ru/'

@pytest.fixture()
def driver():

    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.maximize_window()
    print(f"Зашли на сайт")
    time.sleep(1)
    return driver