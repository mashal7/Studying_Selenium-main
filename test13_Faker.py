import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from re import findall
from faker import Faker

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

faker = Faker('en_US')  # ru_RU

# авторизация
# рандомное имя, чтобы не повторялось (можно прописать имя+дата_время)
name = faker.first_name() + str(faker.random_int())
password = faker.password()
print(name, password)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(name)

password_field = driver.find_element(By.XPATH, "//input[@id='password']")
password_field.send_keys(password)

