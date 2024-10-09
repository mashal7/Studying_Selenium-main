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

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

login_standard_user = 'standard_user'
password_general = 'secret_sauce'

# авторизация
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('input login')

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_general)
print('input password')

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('click button_login')

# создание имени скриншота
now_date = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
name_screenshot = f'C:\\Users\\mpetrova\\Desktop\\Less\\Selenium\\screen\\{now_date}.png'

#driver.execute_script('window.scrollTo(0, 200)')
#time.sleep(3)
#driver.save_screenshot(name_screenshot)

action = ActionChains(driver)
red_sweater = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
action.move_to_element(red_sweater).perform()
time.sleep(3)
driver.save_screenshot(name_screenshot)