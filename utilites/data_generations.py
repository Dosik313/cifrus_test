import random

def random_index(self):
    all_locators = driver.find_elements(By.XPATH,'//div[@class="name"]')
    return random.randint(1, 40)