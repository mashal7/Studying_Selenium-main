import time
from datetime import date, timedelta

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)

# переход на сайт
print('Переход на сайт')
driver.get('https://the-internet.herokuapp.com/key_presses?')
field_date = driver.find_element(By.XPATH, '//input[@id="target"]')
field_date.click()

# ввод текущей даты
pattern = '%d.%m.%Y'
current_date = date.today()
print('Ввод текущей даты')
field_date.send_keys(current_date.strftime(pattern))
time.sleep(3)

# очистка поля
field_date.clear()
time.sleep(3)

# ввод даты + 10 дней
print('Ввод даты + 10 дней')
new_date = current_date + timedelta(days=10)
field_date.send_keys(new_date.strftime(pattern))

