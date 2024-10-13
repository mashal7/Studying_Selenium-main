import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.binary_location = "C:\\Users\\masha\\AppData\\Local\\Programs\\Opera\\opera.exe"

service = Service("C:\\Users\\masha\\OneDrive\\Рабочий стол\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)


driver.get('https://demoqa.com/browser-windows')
driver.maximize_window()

# взаимодействие с окнами браузера
button = driver.find_element(By.XPATH, '//button[@id="windowButton"]')
button.click()
time.sleep(4)
print(driver.current_url)

header1 = driver.find_element(By.XPATH, '//h1[@class="text-center"]') # заголовок с 1 окна
print(header1.text)

windows_1 = driver.window_handles[0]    # переменные для обращения к переходу
windows_2 = driver.window_handles[1]

driver.switch_to.window(windows_2)    # переход на 2-ое окно
print(driver.current_url)

header2 = driver.find_element(By.XPATH, '//h1[@id="sampleHeading"]')  # заголовок со 2 окна
print(header2.text)

driver.switch_to.window(windows_1)     # переход на 1-ое окно
print(driver.current_url)
header1 = driver.find_element(By.XPATH, '//h1[@class="text-center"]') # заголовок с 1 окна
print(header1.text)

