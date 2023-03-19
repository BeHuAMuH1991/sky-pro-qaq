from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Cart:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "span.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a").click()

    def add_cart(self): 
        lag = self._driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div/div/div[1]/ul/li[1]/a/b").text
        
        return int (lag)

