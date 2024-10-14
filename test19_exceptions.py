import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)


driver.get('https://demoqa.com/dynamic-properties')
#driver.maximize_window()

# -------------------неявное ожидание
# неявное ожидание: система ждет появление элемента до 10 сек; действует на весь код
# driver.implicitly_wait(10)
#
# print('Start test')
# visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
# visible_button.click()
# print('Click visible_button')
# print('Finish test')

# -------------------явное ожидание
# явное ожидание: прописывается для каждого элемента и действия индивидуально
print('Start test')
# задаем время, в течение которого будет дожидаться появления элемента и его кликабельности

# Создаем объект WebDriverWait с указанием времени ожидания (например, 30 секунд)
wait = WebDriverWait(driver, 30)

# Ожидаем, пока элемент не станет кликабельным
visible_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="visibleAfter"]')))
visible_button.click()
print('Click visible_button')
print('Finish test')