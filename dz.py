import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from re import findall

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)


class BaseActions:
    '''Базовые действия при работе с сайтом'''

    @staticmethod
    def fill_out_field(xpath, value):
        driver.find_element(By.XPATH, xpath).send_keys(value)

    @staticmethod
    def click_button(name, xpath):
        driver.find_element(By.XPATH, xpath).click()
        print(f'click {name}')


class StepTest:
    '''Основные действия для тестирования сайта'''

    def __init__(self, url):
        self._base_url = url
        self._dict = {}
        driver.get(self._base_url)

    @staticmethod
    def autorization(username, login):
        BaseActions.fill_out_field("//input[@id='user-name']", username)
        BaseActions.fill_out_field("//input[@id='password']", login)
        BaseActions.click_button('Login', "//input[@id='login-button']")
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'Autorization author is not successful'
        print('Autorization author is successful')
        time.sleep(3)

    @staticmethod
    def select_product_to_basket(xpath):
        BaseActions.click_button('Add to cart', xpath)
        print('Product in basket')

    @staticmethod
    def list_of_values_for_check(class_name):
        products = {}
        descriptions = driver.find_elements(by=By.CLASS_NAME, value=class_name)
        for desc in descriptions:
            product_name = desc.find_element(by=By.CLASS_NAME, value='inventory_item_name').text
            product_price = desc.find_element(by=By.CLASS_NAME, value='inventory_item_price').text
            products[product_name] = product_price
        return products

    @staticmethod
    def check_basket(products_from_catalog):
        BaseActions.click_button('basket', '//div[@id="shopping_cart_container"]')
        products_from_backet = StepTest.list_of_values_for_check('cart_item_label')
        for product_name, product_price in products_from_backet.items():
            assert products_from_catalog.get(product_name,
                                             None) == product_price, f'Product {product_name} check not successfully'
            print(f'Product "{product_name}" check successfully')

    @staticmethod
    def making_order(first_name, last_name, postal_code):
        BaseActions.click_button('Checkout', '//button[@id="checkout"]')
        BaseActions.fill_out_field('//input[@id="first-name"]', first_name)
        BaseActions.fill_out_field('//input[@id="last-name"]', last_name)
        BaseActions.fill_out_field('//input[@id="postal-code"]', postal_code)


    @staticmethod
    def check_order(products_from_catalog):
        BaseActions.click_button('Continue', '//input[@id="continue"]')
        products_from_order = StepTest.list_of_values_for_check('cart_item_label')
        for product_name, product_price in products_from_order.items():
            assert products_from_catalog.get(product_name, None) == product_price, f'Product {product_name} check not successfully'
            print(f'Product "{product_name}" check successfully')
        pattern = r'\d+(?:\.\d+)?'
        sum_price = sum(float(i[1:]) for i in products_from_order.values())
        sum_price_checkout = driver.find_element(By.XPATH, '//div[@data-test="subtotal-label"][1]').text
        sum_price_checkout = float(findall(pattern, sum_price_checkout)[0])
        assert sum_price == sum_price_checkout, 'Total price is incorrect'
        print('Total price is correct')

    @staticmethod
    def check_finish_order():
        BaseActions.click_button('Finish', '//button[@id="finish"]')
        complete_text = driver.find_element(By.XPATH, '//h2[@data-test="complete-header"][1]').text
        assert complete_text == 'Thank you for your order!', 'Page is incorrect'
        print('Page is correct')

smoke = StepTest('https://www.saucedemo.com/')

# авторизация
smoke.autorization('standard_user', 'secret_sauce')

# выбор товаров в корзину, товар №2 и товар №3
print('Choose product 2 and 3')
smoke.select_product_to_basket('//button[@id="add-to-cart-sauce-labs-bike-light"]')
smoke.select_product_to_basket('//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

# получаем словарь названий товаров с ценами из каталога
products_from_catalog = StepTest.list_of_values_for_check('inventory_item_description')

# переход в корзину и проверка товаров в корзине
StepTest.check_basket(products_from_catalog)

# переход на оформление заказа и оформление заказа
StepTest.making_order('Ivan', 'Ivanov', '12345')

# проверка товаров и суммы товаров в заказе
StepTest.check_order(products_from_catalog)

# завершение оформления заказа и проверка страницы успешного оформления
StepTest.check_finish_order()