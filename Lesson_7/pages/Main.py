from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.labirint.ru")   
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()        

    def set_cookie_policy(self):
        cookie = {
            "name" : "cookie_policy",
            "value" : "1"
        }
        self._driver.add_cookie(cookie)
    #Найти все книги по слову Python
    def search(self, term):
           
        self._driver.find_element(By.CSS_SELECTOR, "input#search-field").send_keys("term", Keys.RETURN)

        