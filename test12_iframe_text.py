import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from re import findall

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)


driver.get('https://www.lambdatest.com/selenium-playground/iframe-demo/')

# обращение к iframe, т. к. локатор находится в нем
iframe = driver.find_element(By.XPATH, '//iframe[@id="iFrame1"]')
driver.switch_to.frame(iframe)

field = driver.find_element(By.XPATH, '//div[@id="__next"]/div/div[@class="rsw-ce"]')
value_field = field.text
print(value_field)

# поменяем текст на жирный
field.send_keys(Keys.CONTROL + 'a')
editing_panel_bold = driver.find_element(By.XPATH, '//button[@title="Bold"]')
editing_panel_bold.click()

new_field = driver.find_element(By.XPATH, '//div[@id="__next"]/div/div[@class="rsw-ce"]/b')
value_new_field = field.text

# проверка, что значение поля находится в тегах и (жирный текст)
assert value_field == value_new_field, 'Ошибка!'
print('Значение поля осталось верным после редактирования')



# input_field.send_keys(message)
# button = driver.find_element(By.XPATH, '//button[@id="showInput"]')
# button.click()
#
# field_message =  driver.find_element(By.XPATH, '//p[@id="message"]')
# value_message = field_message.text
# assert message == value_message, 'Ошибка!'
# print('Значение верное')
