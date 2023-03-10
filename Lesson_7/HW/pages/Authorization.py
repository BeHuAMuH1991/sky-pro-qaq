from selenium.webdriver.common.by import By
from selenium import webdriver
import allure

@allure.epic("Ввод логина и пароля")
class Authorization:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(5)
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Вводим логин при авторизации")
    def user_name(self, name : str):
        """Вводит логин при авторизации"""
        self._driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(name)

    @allure.step("Вводим пароль при авторизации")
    def password(self, password : str):
        """Вводит пароль при авторизации"""
        self._driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(password)

    @allure.step("Нажимает кнопку \"LOGIN\"")
    def click_login(self : str):
        """Нажимает кнопку \"LOGIN\""""
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()