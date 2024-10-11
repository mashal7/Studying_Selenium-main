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
driver.get('https://www.schoolsw3.com/howto/howto_js_rangeslider.php')

actions = ActionChains(driver)
print('s')
default = driver.find_element(By.XPATH, '//h4[text()="По умолчанию:"]/following-sibling::input[@type="range"]')
actions.click_and_hold(default).move_by_offset(20, 0).release().perform()


