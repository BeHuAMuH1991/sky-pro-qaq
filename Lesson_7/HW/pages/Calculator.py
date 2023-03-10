import allure 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.epic("Работа с калькулятором")
class Calculator:

    def __init__(self, browser):

        self._driver = browser
        self.waiter = WebDriverWait(browser, 46)
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Очищаем поле с временем ожидания и вводим свои данные")
    def waiting_time(self, time: str):
        """Очищаем поле с временем ожидания и вводим свои данные"""
        self._driver.find_element(By.CSS_SELECTOR, "input#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input#delay").send_keys(time)


    @allure.step("Жмем на цифру 7")
    def seven(self):
        """Жмем на цифру 7"""
        a = self._driver.find_element(By.XPATH, "//*[text() ='7']").click()

    @allure.step("Жмем на плюс")
    def plus(self):
        """Жмем на плюс"""
        self._driver.find_element(By.XPATH, "//*[text() ='+']").click()

    @allure.step("Жмем на цифру 8")
    def eigth(self):
        """Жмем на цифру 8"""
        self._driver.find_element(By.XPATH, "//*[text() ='8']").click()

    @allure.step("Жмем на равно")
    def equal(self):
        """Жмем на равно"""
        self._driver.find_element(By.XPATH, "//*[text() ='=']").click()

    @allure.step("Выжидаем время и смотрит какие число высветилось на экране")
    def displey(self) -> str:
        """Выжидаем время и смотрит какие число высветилось на экране"""
        self.waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

        displey = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return displey