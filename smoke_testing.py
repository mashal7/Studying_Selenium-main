import time
from datetime import datetime
from itertools import product

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service, options=options)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

login_standard_user = 'standard_user'
password_general = 'secret_sauce'

# авторизация
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('input login')

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_general)
print('input password')

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('click button_login')

# информация о товаре
product_name = driver.find_element(By.XPATH, '//div[@data-test="inventory-item-name"]').text
product_price = driver.find_element(By.XPATH, '//div[@data-test="inventory-item-price"]').text
print(product_name, product_price, sep='\n')

# кладём товар в корзину и переходим в неё
select_product = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product.click()
print('select product')
to_basket = driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
to_basket.click()
print('to basket')

# сравниваем инфомацию о товаре в каталоге и корзине
product_name_basket = driver.find_element(By.XPATH, '//div[@data-test="inventory-item-name"]').text
product_price_basket = driver.find_element(By.XPATH, '//div[@data-test="inventory-item-price"]').text

assert product_name_basket == product_name, 'Названия товаров не совпадают'
print('Названия товаров совпадают')
assert product_price_basket == product_price, 'Цены товаров не совпадают'
print('Цены товаров совпадают')

# оформление зазака
to_checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
to_checkout.click()
print('переход на оформление')

first_name_string, last_name_string, zip_string = 'Ivan', 'Ivanov', '1234'
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys(first_name_string)

last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys(last_name_string)

zip = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
zip.send_keys(zip_string)

to_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
to_continue.click()
print('нажатие continue')

# сравниваем инфомацию о товаре в каталоге и после оформления
product_name_checkout = driver.find_element(By.XPATH, '//div[@data-test="inventory-item-name"]').text
product_price_checkout = driver.find_element(By.XPATH, '//div[@data-test="inventory-item-price"]').text
sum_price_checkout = driver.find_element(By.XPATH, '//div[@data-test="subtotal-label"][1]').text

assert product_name_checkout == product_name, 'Названия товаров не совпадают'
print('Названия товаров совпадают')
assert product_price_checkout == product_price, 'Цены товаров не совпадают'
print('Цены товаров совпадают')
assert sum_price_checkout == f'Item total: {product_price}', 'Итоговая цена не совпадает'
print('Итоговая цена совпадает')

# завершение оформления заказа
to_continue = driver.find_element(By.XPATH, '//button[@id="finish"]')
to_continue.click()
print('нажатие finish')

# проверка страницы успешного оформления
complete_text = driver.find_element(By.XPATH, '//h2[@data-test="complete-header"][1]').text
assert complete_text == 'Thank you for your order!', 'Страница не верная'
print('Страница верная')