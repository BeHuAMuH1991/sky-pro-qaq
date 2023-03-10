from selenium.webdriver.common.by import By
import allure

@allure.epic("Кладем товары в корзину")
class Buy:
    def __init__(self, browser):
        self._driver = browser
       
    @allure.step("Кладет в корзину рюкзак")
    def buy_backpack(self):
        """Кладем в корзину рюкзак"""
        self._driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()

    @allure.step("Кладем в корзину шорты") 
    def buy_shirt(self):
        """Кладем в корзину шорты"""
        self._driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()

    @allure.step("Кладем в корзину комбинезон") 
    def buy_onesie(self):
        """Кладем в корзину комбинезон"""
        self._driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()

    @allure.step("Жмем кнопку корзина") 
    def click_cart(self):
        """Жмем кнопку корзина"""
        self._driver.find_element(By.CSS_SELECTOR, "div#shopping_cart_container").click()
