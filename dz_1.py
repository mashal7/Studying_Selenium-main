from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from smoke_testing import product_name, product_price

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

class BaseActions:
    @staticmethod
    def fill_out_field(xpath, value):
        driver.find_element(By.XPATH, xpath).send_keys(value)

    @staticmethod
    def click_button(name, xpath):
        driver.find_element(By.XPATH, xpath).click()
        print(f'click {name}')

    @staticmethod
    def return_value_of_obj(xpath):
        return driver.find_element(By.XPATH, xpath).text

class SmokeTest:
    def __init__(self, url):
        self._base_url = url
        driver.get(self._base_url)

    @staticmethod
    def autorization(username, login):
        BaseActions.fill_out_field("//input[@id='user-name']", username)
        BaseActions.fill_out_field("//input[@id='password']", login)
        BaseActions.click_button('Login', "//input[@id='login-button']")
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'Авторизация не прошла'
        print('Авторизация прошла успешно')

    @staticmethod
    def select_product_to_basket(xpath):
        product_name=driver.find_element(By.XPATH, '//div[@data-test="inventory-item-name"]').text
        product_price=
        BaseActions.click_button('Add to cart', xpath)




smoke = SmokeTest('https://www.saucedemo.com/')
smoke.autorization('standard_user', 'secret_sauce')
select_product_to_basket('//button[@id="add-to-cart-sauce-labs-bike-light"]')