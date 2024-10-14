import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
time.sleep(3)

# загрузка файлов в браузер
button_load_file = driver.find_element(By.XPATH, '//input[@id="file"]')
path_file = r'C:\Users\mpetrova\Desktop\screen.png'
button_load_file.send_keys(path_file)


