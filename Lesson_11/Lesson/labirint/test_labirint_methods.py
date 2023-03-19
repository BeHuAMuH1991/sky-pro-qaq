from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.Result import Result
from pages.Main import Main
from pages.Cart import Cart


def test_cart_counter(driver):
    
    main = Main(driver)
    main.set_cookie_policy()
    main.search("Python")

    result = Result(driver)
    result.table()
    added = result.add_books()

    cart = Cart(driver)
    cart.open_cart()
    l = cart.add_cart()
    
    assert added == l