from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Main:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.get("https://www.labirint.ru/")


    def set_cookie_policy(self):
        cookie = {
            "name" : "cookie_policy",
            "value" : "1"
        }
        self._driver.add_cookie(cookie)

    def search(self, tern: str):
        self._driver.find_element(By.CSS_SELECTOR, "input#search-field").send_keys(tern, Keys.RETURN)