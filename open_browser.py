import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options, service=service)

# Открываем веб-страницу и разворачиваем окно
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
#driver.maximize_window()

# обращение по full XPATH
#user_name = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input')

# обращение по name
# password = driver.find_element(By.NAME, 'password')
# password.send_keys('secret_sauce')


# обращение по id
user_name = driver.find_element(By.ID, 'user-name')
#user_name = driver.find_elements_by_id('user-name')
user_name.send_keys('standard_user')

# обращение по id XPATH
#password = driver.find_element(By.XPATH, "//input[@id='password']")

# обращение по CSS Selector
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')

#вход через кнопу login
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()



