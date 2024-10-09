import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# режим без открытия браузера


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
password.send_keys(Keys.RETURN)     #Enter

filter = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
filter.click()
print('input filter')
time.sleep(3)
filter.send_keys(Keys.DOWN)
time.sleep(3)
filter.send_keys(Keys.ENTER)

# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print('click button_login')

