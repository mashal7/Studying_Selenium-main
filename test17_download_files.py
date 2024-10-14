import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# ----------------укажем в настройках браузера директорию по умолчанию, куда будет скачиваться файл
path_download = 'C:\\Users\\mpetrova\\Desktop\\Less\\Selenium\\file_downloads\\'
prefs = {'download.default_directory' : path_download}
options.add_experimental_option('prefs', prefs)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)

base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)

# -----------------загрузка файлов с браузера в папку
#button_download_file = driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
button_download_file = driver.find_element(By.XPATH, '//button[contains(text(), "Download File")]')
button_download_file.click()
time.sleep(6)

# -----------------проверяем содержимое папки со скачанным на наличие файлов
print('Папка не пустая' if os.listdir(path_download) else 'Папка пустая')

# -----------------выводим содержимое папки
print(os.listdir(path_download))

# ----------------проверяем содержимое папки со скачанным на наличие определенного файла
file_name = 'LambdaTest.pdf'
file_path = path_download + file_name

assert os.access(file_path, os.F_OK), 'Такого файла нет в директории'
print('Файл в директории')

# ---------проверяем, не пустые ли файлы в папке
# glob.glob(pattern) — Возвращает список файлов и директорий, соответствующих шаблону
files = glob.glob(os.path.join(path_download, '*.*'))   #os.path.join(path, *paths) — Соединяет компоненты пути в одну строку.

for file in files:
    print('Файл не пустой' if os.path.getsize(file) > 10 else 'Файл пустой')    # если весит < 10 кбайт, то пустой

# ------------Очистка директории по файлам
#files = glob.glob(os.path.join(path_download, '*.*'))
for file in files:
    os.remove(file)

# ---------------проверяем содержимое папки со скачанным на наличие файлов
print('Папка не пустая' if os.listdir(path_download) else 'Папка пустая')








