from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Настраиваем опции браузера
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)     #не позволит браузеру закрыться

# Указываем путь к ChromeDriver
#driver = webdriver.Chrome(executable_path='C:\\Users\\mpetrova\\Desktop\\Less\\Selenium\\chromedriver.exe', options=options)

# Инициализация WebDriver с автоматической установкой ChromeDriver
service = ChromeService(ChromeDriverManager().install())

# Создаем экземпляр драйвера с использованием сервиса и опций
driver = webdriver.Chrome(service=service, options=options)

# Открываем веб-страницу и разворачиваем окно
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()