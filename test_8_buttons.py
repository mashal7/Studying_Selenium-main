import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
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

base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
driver.get(base_url)

# check box - галочки, можно выбрать несколько
check_box = driver.find_element(By.XPATH, '//input[@value="cb1"]')
check_box.click()
check_box = driver.find_element(By.XPATH, '//input[@value="cb3"]')

if check_box.is_selected():
    print("Чек-бокс выбран")
else:
    print("Чек-бокс не выбран")

check_box.click()



# radio items (buttons) - кружок, можно выбрать только один
radio_item = driver.find_element(By.XPATH, '//input[@value="rd1"]')
radio_item.click()
time.sleep(2)
radio_item = driver.find_element(By.XPATH, '//input[@value="rd3"]')
radio_item.click()

# radio items (buttons) - кружок, можно выбрать только один
radio_item = driver.find_element(By.XPATH, '//input[@value="rd1"]')
radio_item.click()
time.sleep(2)
radio_item = driver.find_element(By.XPATH, '//input[@value="rd3"]')
radio_item.click()

# двойной клик
action = ActionChains(driver)
locator = driver.find_element(By.XPATH, '//select[@name="dropdown"]') # локатор
action.double_click(locator).perform()  # perform для сохранения действия

# клик правой кнопкой мыши
action = ActionChains(driver)
locator = driver.find_element(By.XPATH, '//select[@name="dropdown"]') # локатор
action.context_click(locator).perform()  # perform для сохранения действия