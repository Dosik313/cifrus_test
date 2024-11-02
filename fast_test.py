import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilites.locators import Locators

driver = webdriver.Chrome()
driver.get('https://www.cifrus.ru/')
driver.maximize_window()

time.sleep(2)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.YOU_CITY_ENTER))).click()
print(f"клик успешен")
time.sleep(2)



all_locators = driver.find_elements(By.XPATH,'//div[@class="name"]')
print(len(all_locators))