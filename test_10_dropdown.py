import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service, options=options)

def test1():
    base_url = 'https://www.saucedemo.com/'
    driver.get(base_url)

    login_standard_user = 'standard_user'
    password_general = 'secret_sauce'

    # авторизация
    user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
    user_name.send_keys(login_standard_user)
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys(password_general)
    button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
    button_login.click()

    # drop_down
    select = Select(driver.find_element(By.XPATH, '//select[@class="product_sort_container"]'))
    #select.select_by_visible_text('Name (Z to A)')
    select.select_by_value('za')


def test2():
    base_url = 'https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
    driver.get(base_url)

    # drop_down
    # drop_down = driver.find_element(By.XPATH, '//span[@aria-labelledby="select2-country-container"]')
    # drop_down.click()
    #
    # select_country = driver.find_element(By.XPATH, '(//li[@class="select2-results__option"])[2]')
    # select_country.click()

    drop_down = driver.find_element(By.XPATH, '(//input[@class="select2-search_field"])[2]')
    # //span[@class="select2-dropdown select2-dropdown--below"]//input[@class="select2-search_field"]
    #drop_down.click()
    drop_down.send_keys('Australia')
    drop_down.send_keys(Keys.ENTER)

test2()

