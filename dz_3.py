import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from re import findall
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

class MakeOrder:
    '''Действия при работе с сайтом'''

    # вход на сайт
    @staticmethod
    def enter_site():
        print('Вход на сайт "https://www.saucedemo.com/"')
        driver.get('https://www.saucedemo.com/')

    # метод для заполнения поля
    @staticmethod
    def fill_out_field(xpath, value):
        driver.find_element(By.XPATH, xpath).send_keys(value)

    # метод для нажатия кнопки
    @staticmethod
    def click_button(name, xpath):
        driver.find_element(By.XPATH, xpath).click()
        print(f'Нажать "{name}"')

    # метод для авторизации
    @staticmethod
    def autorization(username, login):
        print('------------------\nПроверка авторизации')
        MakeOrder.fill_out_field("//input[@id='user-name']", username)
        MakeOrder.fill_out_field("//input[@id='password']", login)
        MakeOrder.click_button('Login', "//input[@id='login-button']")
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'Ошибка авторизации'
        print('Авторизация прошла успешно\n-------------------------\n')
        print('Приветствую тебя в нашем интернет-магазине')

    # метод для получения информации по товарам с помощью имени класса
    @staticmethod
    def list_of_values_for_check(class_name):
        products = {}
        wait = WebDriverWait(driver, 20)
        descriptions = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, class_name)))
        #descriptions = driver.find_elements(by=By.CLASS_NAME, value=class_name)
        for desc in descriptions:
            product_name = desc.find_element(by=By.CLASS_NAME, value='inventory_item_name').text
            product_price = desc.find_element(by=By.CLASS_NAME, value='inventory_item_price').text
            products[product_name] = product_price
        return products

    # метод для добавления товара в корзину
    @staticmethod
    def select_product_to_basket(xpath):
        print('------------------\nДобавление товара в корзину')
        MakeOrder.click_button('Add to cart', xpath)

    # метод для проверки информации о товарах в корзине с товарами из каталога
    @staticmethod
    def check_basket(products_from_catalog):
        print('------------------\nСравнение информации о товарах в корзине с товарами из каталога')
        MakeOrder.click_button('basket', '//div[@id="shopping_cart_container"]')
        products_from_backet = MakeOrder.list_of_values_for_check('cart_item_label')
        for product_name, product_price in products_from_backet.items():
            assert products_from_catalog.get(product_name, None) == product_price, f'Информация о товаре "{product_name}" в корзине не совпадает с информацией в каталоге'
            print(f'Информация о товаре "{product_name}" в корзине указана верно')
        print('Информация о товарах в корзине указана верно\n-------------------------\n')

    # метод для оформления заказа
    @staticmethod
    def making_order(first_name, last_name, postal_code):
        print('--------------------\nОформление заказа')
        MakeOrder.click_button('Checkout', '//button[@id="checkout"]')
        MakeOrder.fill_out_field('//input[@id="first-name"]', first_name)
        MakeOrder.fill_out_field('//input[@id="last-name"]', last_name)
        MakeOrder.fill_out_field('//input[@id="postal-code"]', postal_code)

    # метод для проверки информации о товарах в заказе с товарами из каталога
    @staticmethod
    def check_order(products_from_catalog):
        print('------------------\nСравнение информации о товарах в заказе с товарами из каталога')
        MakeOrder.click_button('Continue', '//input[@id="continue"]')
        products_from_order = MakeOrder.list_of_values_for_check('cart_item_label')
        for product_name, product_price in products_from_order.items():
            assert products_from_catalog.get(product_name, None) == product_price, f'Информация о товаре "{product_name}" в заказе не совпадает с информацией в каталоге'
            print(f'Информация о товаре "{product_name}" в заказе указана верно')
        pattern = r'\d+(?:\.\d+)?'
        sum_price = sum(float(i[1:]) for i in products_from_order.values())
        sum_price_checkout = driver.find_element(By.XPATH, '//div[@data-test="subtotal-label"][1]').text
        sum_price_checkout = float(findall(pattern, sum_price_checkout)[0])
        assert sum_price == sum_price_checkout, 'Полная сумма заказа указа не верно'
        print('Полная сумма заказа указа верно\n-------------------------\n')

    # метод для проверки страницы об успешном завершении заказа
    @staticmethod
    def check_finish_order():
        print('------------------\nПроверка страницы об успешном завершении заказа')
        MakeOrder.click_button('Finish', '//button[@id="finish"]')
        complete_text = driver.find_element(By.XPATH, '//h2[@data-test="complete-header"][1]').text
        assert complete_text == 'Thank you for your order!', 'Ошибка! не удалось успешно завершить заказ'
        print('Заказ успешно завершен\n-------------------------\n')


#================================================================================
make_order = MakeOrder()
make_order.enter_site()

# --------------авторизация
make_order.autorization('standard_user', 'secret_sauce')

# --------------выбор товаров в корзину
#  получаем информацию обо всех товарах из каталога
products_from_catalog = make_order.list_of_values_for_check('inventory_item_description')
products = {i: k for i, k in enumerate(products_from_catalog.keys(), 1)}
# выбираем нужные нам товары
print('Выбери один или несколько из следующих товаров и укажи их номера: ')
for k, v in products.items():
    print(f'{k}: {v}')
product = list(map(int, input('\nВведите номера через пробел: ').split()))
# кладем товары в корзину
try:
    assert product != [], 'Товары не выбраны'
    for key in product:
        id = products[key].lower().replace(' ', '-')
        make_order.select_product_to_basket(f'//button[@id="add-to-cart-{id}"]')
        print(f'Товар {products[key]} в корзине\n-------------------------\n')
except KeyError as err:
    print(f'Товара {key} не существует')
    raise err

# ---------------переход в корзину и проверка товаров в корзине
make_order.check_basket(products_from_catalog)

# ---------------переход на оформление заказа и оформление заказа
make_order.making_order('Ivan', 'Ivanov', '12345')

# -----------------проверка товаров и суммы товаров в заказе
make_order.check_order(products_from_catalog)

# ------------------завершение оформления заказа и проверка страницы успешного оформления
make_order.check_finish_order()