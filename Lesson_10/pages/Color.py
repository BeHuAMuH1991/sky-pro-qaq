import allure
from selenium.webdriver.common.by import By

@allure.epic("Проверка цвета полей")
class Color:

    def __init__(self, browser):

        self._driver = browser
        self._driver.fullscreen_window()

    @allure.step("Смотрим какого цвета поле\"ZIP\"")
    def color_zip(self) -> str:
        """Смотрим какого цвета поле \"ZIP\""""
        color_zip = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
        return color_zip

    @allure.step("Смотрим какого цвета поле \"Company\"")
    def color_company(self) -> str:
        """Смотрим какого цвета поле Company"""
        color_company = self._driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")
        return color_company

    @allure.step("Смотрим какого цвета поле \"Job\"")
    def color_job_position(self) -> str:
        """Смотрим какого цвета поле \"job\""""
        color_job_position = self._driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")
        return color_job_position

    @allure.step("Смотрим какого цвета поле \"Phone\"")
    def color_phone_number(self) -> str:
        """Смотрим какого цвета поле"""
        color_phone_number = self._driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")
        return color_phone_number

    @allure.step("Смотрим какого цвета поле \"E-mail\"")
    def color_e_mail(self) -> str:
        """Смотрим какого цвета поле"""
        color_e_mail = self._driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")
        print(color_e_mail)
        return color_e_mail

    @allure.step("Смотрим какого цвета поле \"Country\"")
    def color_country(self) -> str:
        """Смотрим какого цвета поле"""
        color_country = self._driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")
        return color_country

    @allure.step("Смотрим какого цвета поле \"City\"")
    def color_city(self) -> str:
        """Смотрим какого цвета поле"""
        color_city = self._driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")
        return color_city

    @allure.step("Смотрим какого цвета поле \"Address\"")
    def color_address(self) -> str:
        """Смотрим какого цвета поле"""
        color_address = self._driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")
        return color_address

    @allure.step("Смотрим какого цвета поле \"Last name\"")
    def color_last_name(self) -> str:
        """Смотрим какого цвета поле"""
        color_last_name = self._driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")
        return color_last_name

    @allure.step("Смотрим какого цвета поле \"First name\"")
    def color_first_name(self) -> str:
        """Смотрим какого цвета поле"""
        color_first_name = self._driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
        return color_first_name