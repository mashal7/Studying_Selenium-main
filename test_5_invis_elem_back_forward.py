import time
from datetime import datetime

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

# скрытое меню
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(2)

link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
# assert driver.current_url == 'https://saucelabs.com/', 'Ошибка'
# print('Адрес верный')
# print(driver.current_url)
driver.back()
print('Go back')
time.sleep(3)
driver.forward()
print('Go forward')