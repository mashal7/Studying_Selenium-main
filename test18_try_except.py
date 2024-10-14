import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)


#driver.get('https://demoqa.com/dynamic-properties')
#driver.maximize_window()

# # -------------------взаимодействие с ожиданиями через исключение
# try:
#     visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
#     visible_button.click()
#     print('Click visible_button')
# except NoSuchElementException as err:
#     print('NoSuchElementException')
#     time.sleep(7)
#     visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
#     visible_button.click()
#     print('Click visible_button')

# -------------------работа с проверками через исключение
driver.get('https://demoqa.com/radio-button')
radio_button_yes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
radio_button_yes.click()
time.sleep(7)
try:
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]').text
    print(message)
    assert message == 'No'
except AssertionError as err:
    print(err)
    driver.refresh()        # перезагрузка страницы
    time.sleep(7)
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]').text
    print(message)
    assert message == 'Yes'
    print('radio button = Yes')
print('Test over')


