import time
from dbm import error
from faulthandler import is_enabled

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# режим без открытия браузера
#options.add_argument('--headless=new')
#options.add_argument('--headless=old')

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

# проверка на неправильную авторизацию (негативный тест)
warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_text = warring_text.text
print(value_warning_text)
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service', 'Авторизация прошла успешно'
print('Ошибка авторизации. Сообщение корректно')

# проверка по кликабельности элемента (для того, чтобы можно было закрыть сообщение, мы можем осуществить проверку о наличии сообщения об ошибке)
# error_button = driver.find_element(By.XPATH, "//button[@data-test='error-button']")
# time.sleep(3)
# error_button.click()
# print('Click Error Button')
# try:
#     driver.find_element(By.XPATH, "//h3[@data-test='error']")
# except:
#     print('Элемент кликабелен')

# button_x = driver.find_element(By.XPATH, "//h3[@data-test='error']")
# print(button_x.is_enabled())