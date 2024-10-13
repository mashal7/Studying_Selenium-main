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


driver.get('https://www.lambdatest.com/selenium-playground/simple-form-demo')

# message = 'Hello'
# input_field = driver.find_element(By.XPATH, '//input[@id="user-message"]')
# input_field.send_keys(message)
# button = driver.find_element(By.XPATH, '//button[@id="showInput"]')
# button.click()
#
# field_message =  driver.find_element(By.XPATH, '//p[@id="message"]')
# value_message = field_message.text
# assert message == value_message, 'Ошибка!'
# print('Значение верное')

num1, num2 = 2, 3
input_field = driver.find_element(By.XPATH, '//input[@id="sum1"]')
input_field.send_keys(num1)
input_field = driver.find_element(By.XPATH, '//input[@id="sum2"]')
input_field.send_keys(num2)
button = driver.find_element(By.XPATH, '//button[contains(text(), "Get Sum")]')
button.click()

field_sum = driver.find_element(By.XPATH, '//p[@id="addmessage"]')
value_sum = field_sum.text
assert str(num1 + num2) == value_sum, 'Ошибка!'
print('Значение верное')