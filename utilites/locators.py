

class Locators:
    """Класс со всеми локаторами приложения"""

    """Локаторы главной страницы"""

    YOU_CITY_ENTER = '(//a[@id="1"])[3]'   # Выбрать город вначале, Москва
    all_category = '//button[@class="btn-category dropdown-toggle"]' # клик по кнопке все категории


    """Локаторы страницы с выбором товара"""

    all_name_locators = '//div[@class="name"]'
    name_item = '(//div[@class="name"])'
    price_item = '(//span[@class="price-new"])'
    add_to_cart_item = '(//button[@class="btn main-btn"])'

    check_title_before_cart = '//p[@class="head"]'
    check_price_before_cart = '//*[@id="OrderContainer"]/div/center/div/div/div[2]/div[1]/p'

    ENTER_CART_BONNON = '(//a[@href="/basket.php"])[2]'

    """Локаторы в корзине"""

    CART_PAGE_TITLE = '//h1[@class="title-page"]'
    TITLE_ITEM_IN_CART = '//td[@class="name"]//a'
    PRICE_ITEM_IN_CART = '(//span[@class="num"])[1]'
    PRICE_ALL_ITEMS_IN_CART = '//*[@id="total_sub_total"]/span[2]/nobr'
    DELIVERY_PRICE = '//span[@id="del_price"]'
    TOTAL_PRICE = '//span[@id="total_price"]'
    INPUT_USER_INFO = '//input[@class="simplecheckout-red-border"]'
