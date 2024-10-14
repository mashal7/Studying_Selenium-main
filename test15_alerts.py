import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.binary_location = "C:\\Users\\\mpetrova\\AppData\\Local\\Programs\\Opera\\opera.exe"

service = Service("C:\\Users\\mpetrova\\Desktop\\Less\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service)


driver.get('https://the-internet.herokuapp.com/javascript_alerts')
#driver.maximize_window()

# -------------------взаимодействие с всплывающими уведомлениями
# button = driver.find_element(By.XPATH, '//button[@onclick="jsAlert()"]')
# button.click()
# time.sleep(3)
#
# # закрытие уведомление (соглашение)
# driver.switch_to.alert.accept()
#
# try:
#     driver.find_element(By.XPATH, '//p[@id="result"]')
#     print('Успешно')
# except:
#     print('Ошибка выполнения')

# -------------------------взаимодействие с всплывающими сообщениями с двумя выборами
# button = driver.find_element(By.XPATH, '//button[@onclick="jsConfirm()"]')
# button.click()
# time.sleep(3)
#
# # закрытие уведомление (соглашение и отклонение)
# #driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

# -------------------------взаимодействие с всплывающими сообщениями с двумя выборами
button = driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]')
button.click()
time.sleep(3)

# -------------------------------------Переключаемся на всплывающее окно promt (с прописным окном)
# alert = Alert(button)
#
# # Ввод текста в поле всплывающего окна
# alert.send_keys("This is a test input")
# time.sleep(3)
#
# # Подтверждение окна (нажатие "OK")
# alert.accept()

alert = driver.switch_to.alert
alert.send_keys("Текст для ввода")
time.sleep(3)
alert.accept()