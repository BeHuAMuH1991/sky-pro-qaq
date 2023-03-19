import allure
from selenium.webdriver.common.by import By

@allure.epic("Корзина")
class Cart:
    def __init__(self, browser):
        self._driver = browser
    
    @allure.step("Нажимает на кнопку CHECKOUT")
    def checkout(self) -> None:
        """Нажимает на кнопку CHECKOUT"""
        self._driver.find_element(By.CSS_SELECTOR, "button#checkout").click()