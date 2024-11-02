


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

    ENTER_CART_BUTTON = '(//a[@href="/basket.php"])[2]'

    """Локаторы в корзине"""

    CART_PAGE_TITLE = '//h1[@class="title-page"]'
    TITLE_ITEM_IN_CART = '//td[@class="name"]//a'
    PRICE_ITEM_IN_CART = '(//span[@class="num"])[1]'
    COMMISSION = '//span[@id="proc_sp"]'
    PRICE_ALL_ITEMS_IN_CART = '//*[@id="total_sub_total"]/span[2]/nobr'
    DELIVERY_PRICE = '//span[@id="del_price"]'
    TOTAL_PRICE = '//span[@id="total_price"]'
    INPUT_USER_INFO = '//input[@class="simplecheckout-red-border"]'
    INPUT_NAME_USER = '(//input[@class="simplecheckout-red-border"])[1]'
    INPUT_EMAIL_USER = '(//input[@class="simplecheckout-red-border"])[2]'
    INPUT_NUMBER_USER = '//input[@id="checkout_customer_main_telephone"]'
    INPUT_DELIVERY_METHOD = f"(//input[@type='radio'])" # от 1 до 7 вкл.
    INPUT_DELIVERY_CDEK = "//label[@for='shipping6' and contains(text(), 'СДЭК')]"
    INPUT_PICKUP = "//label[contains(text(), 'самовывоз (ул. 2-я Филёвская, 15/19)')]"
    TEXT_PICKUP_ORDER = "//span[contains(text(), 'самовывоз (ул. 2-я Филёвская, 15/19)')]"
    QR_WINDOW_INFO = '//button[@aria-hidden="true"]'
    ADDRESS_CHECK = "//div[@class='simplecheckout-block-heading' and text()='Адрес']"
    INPUT_PAYMENT_METHOD = '(//input[@name="payment_method"])' # от 1 до 3 вкл
    INPUT_CASH_PAYMENT = "//label[contains(text(), 'Наличными')]"
    TEXT_CHECK_CASH_PAYMENT = "//b[contains(text(), 'Инструкция для оплаты Наличными')]"
    TEXT_BANK_PAYMENT = "//b[contains(text(), 'Инструкция для оплаты Дебетовой картой через Сбербанк Онлайн')]"
    TEXT_QR_PAYMENT = "//b[contains(text(), 'Инструкция для оплаты Банковской картой по Системе быстрых платежей по QR (комиссия 5%)')]"
    TEXT_LEGAL_ENTITIES = "//div[contains(text(), 'Реквизиты')]"
    CONFIRM_BUTTON = '//input[@id="simplecheckout_button_confirm"]'

    """Локаторы для заполнения данных о доставке"""

    INPUT_CITY_DELIVERY = '//input[@placeholder="Например, Киров"]'
    INPUT_CURRENT_CITY = '//div[@class="ui-menu-item-wrapper"]'
    INPUT_ADDRESS_DELIVERY = '//input[@id="checkout_customer_main_address_1"]'
    INPUT_DETAILS_CASHLESS = '(//input[@name="bez_bank_id"])' # от 1 до 2 вкл
    INPUT_ORGANIZATION_NAME = '(//input[@class="simplecheckout-red-border"])[5]'
    INPUT_INN = '(//input[@class="simplecheckout-red-border"])[6]'
    INPUT_ENTITIES_ADDRESS = '(//input[@class="simplecheckout-red-border"])[10]'