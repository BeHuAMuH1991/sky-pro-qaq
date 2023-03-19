import allure
from selenium.webdriver.common.by import By

@allure.epic("Подтверждение заказа")
class Checkout:
    def __init__(self, browser):
        self._driver = browser
    
    @allure.step("Смотрим итоговую цену товара")
    def checkout(self) -> int:
        """Смотрим итоговую цену товара"""
        res = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return res
        