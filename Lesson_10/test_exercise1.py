from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure
from pages.Pasty import Pole
from pages.Color import Color
from time import sleep






@allure.title("Проверка цвета в в полях")
def test_color():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    pole = Pole(driver)
    pole.first_name("Иван")
    pole.last_name("Petrov")
    pole.address("Конева 5")
    pole.city("Kirov")
    pole.country("Russia")
    pole.mail("213765@gmil.com")
    pole.phone("89122223355")
    pole.job("QA")
    pole.company("SkyPro")
    pole.click()
    color = Color(driver)
    zip = color.color_zip()
    first = color.color_first_name()
    last = color.color_last_name()
    address = color.color_address()
    city = color.color_city()
    country = color.color_country()
    mail = color.color_e_mail()
    company = color.color_company()
    job = color.color_job_position()
    phone = color.color_phone_number()

    driver.quit()


    assert zip == "rgba(132, 32, 41, 1)"
    assert first == "rgba(15, 81, 50, 1)"
    assert last == "rgba(15, 81, 50, 1)"
    assert address == "rgba(15, 81, 50, 1)"
    assert city == "rgba(15, 81, 50, 1)"
    assert country == "rgba(15, 81, 50, 1)"
    assert mail == "rgba(15, 81, 50, 1)"
    assert company == "rgba(15, 81, 50, 1)"
    assert job == "rgba(15, 81, 50, 1)"
    assert phone == "rgba(15, 81, 50, 1)"





    


