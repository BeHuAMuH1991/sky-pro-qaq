from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.Calculator import Calculator
from time import sleep
import allure





browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@allure.title("Работа калькулятора")
def test_calculator():
    calculator  = Calculator(browser)
    calculator.waiting_time("4")
    calculator.seven()
    calculator.plus()
    calculator.eigth()
    calculator.equal()
    displey = calculator.displey()

    assert displey == "15"
   