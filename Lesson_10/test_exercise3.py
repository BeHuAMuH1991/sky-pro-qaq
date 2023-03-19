import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.Authorization import Authorization
from pages.Buy import Buy
from pages.Cart import Cart
from pages.Data_entry import Entry
from pages.Checkout_overview import Checkout



@allure.title("Покупка вещей")
def test_buy():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    authorization = Authorization(browser)
    authorization.user_name("standard_user")
    authorization.password("secret_sauce")
    authorization.click_login()
    buy_cart = Buy(browser)
    buy_cart.buy_backpack()
    buy_cart.buy_onesie()
    buy_cart.buy_shirt()
    buy_cart.click_cart()
    cart = Cart(browser)
    cart.checkout()
    entry = Entry(browser)
    entry.data_entry("Ванька", "Петров", "612345")
    entry.continues()
    checkout = Checkout(browser)
    result = checkout.checkout()
    browser.quit()

    assert result == "Total: $58.29"