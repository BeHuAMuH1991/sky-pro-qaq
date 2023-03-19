from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

cookie = {
    "name" : "cookie_policy",
    "value" : "1"
}

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Перейти на сайт лабиринт
def open_labirint():
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.add_cookie(cookie)
#Найти все книги по слову 
def search(tern):
    browser.find_element(By.CSS_SELECTOR, "input#search-field").send_keys(tern, Keys.RETURN)

#Переключится на таблицу
def table():
    #Переключится на таблицу
    browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div/form/div[1]/div[1]/div/div/span[6]/span/a[2]").click()

#Добавить все книги в корзину и посчитать сколько их
def add_books():
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located( (By.CSS_SELECTOR, 'table') )
    )
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    
    return counter

#Перейти в корзину
def open_cart():
    browser.find_element(By.CSS_SELECTOR, "span.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a").click()

def add_cart(): 
    lag = browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div/div/div[1]/ul/li[1]/a/b").text
    
    return int (lag)
#Закрыть браузер
def closed_labirint():
    
     browser.quit()


def test_cart_counter():
    open_labirint()
    search("Python")
    table()
    added = add_books()
    open_cart()
    l = add_cart()
    closed_labirint()
    assert added == l