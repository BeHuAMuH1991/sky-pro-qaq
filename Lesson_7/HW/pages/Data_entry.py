import allure
from selenium.webdriver.common.by import By

@allure.epic("Доставка")
class Entry:
    def __init__(self, browser):
        self._driver = browser


    @allure.step("Вводит имя, фамилию и индекс")
    def data_entry(self, first_name :str, last_name :str, zip :str):
        """Вводит имя, фамилию и индекс"""

        self._driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys(zip)

    @allure.step("Наимает на кнопку CONTINUES")
    def continues(self):
        """Наимает на кнопку CONTINUES"""
        self._driver.find_element(By.CSS_SELECTOR, "input#continue").click()