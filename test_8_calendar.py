import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# режим без открытия браузера
#options.add_argument('--headless=new')
# options.add_argument('--headless=old')
driver = webdriver.Chrome(service=service, options=options)

base_url = 'https://fincalculator.ru/kalkulyator-dnej?ysclid=lnbpcpoo7797276405'
driver.get(base_url)

#
from_data = driver.find_element(By.XPATH, '//input[@name="start.value"]')
from_data.clear()       # если поле не пустое
from_data.send_keys('01.10.2024')
time.sleep(2)
from_data.send_keys(Keys.ENTER)
#from_data.click()
day_15 = driver.find_element(By.XPATH, '(//td[@class="day"])[14]')  #'(//td[@class="day" and text()="15"]'
day_15.click()

# //td[contains(@class, "day")]

