import allure
from selenium.webdriver.common.by import By

@allure.epic("Ввод дынных")
class Pole:
    def __init__(self, browser):

        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(5)
        self._driver.fullscreen_window()

    @allure.step("Вводим имя")
    def first_name(self, name : str):
        """Вводим имя"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(name)

    @allure.step("Вводим фамилию")
    def last_name(self, name : str):
        """Вводим фамилию"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(name)

    @allure.step("Вводим улицу")
    def address(self, address : str):
        """Вводим название улицы"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(address)

    @allure.step("Вводим название города")
    def city(self, city : str):
        """Вводим название города"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(city)

    @allure.step("Вводим название страны")
    def country(self, country : str):
        """Вводим название страны"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(country)

    @allure.step("Вводим емайл")
    def mail(self, mail : str):
        """Вводим емайл"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(mail)

    @allure.step("Вводим номер телефона")
    def phone(self, phone : str):
        """Вводим номер телефона"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(phone)

    @allure.step("Вводим название должности")
    def job(self, job : str):
        """Вводим название должности"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(job)

    @allure.step("Вводим название компании в которой работаем")
    def company(self, company : str):
        """Вводим название компании в которой работаем"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(company)

    @allure.step("Вводим индекс")
    def zip(self, zip : str):
        """Вводим индекс"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(zip)
        
    @allure.step("Жмем кнопку 'Submit'")
    def click(self):
        """Жмем кнопку Submit"""
        self._driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    
    
