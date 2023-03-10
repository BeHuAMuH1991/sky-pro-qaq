from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys

cookie = {
    "name" : "cookie_policy",
    "value" : "1"
}

def test_cart_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #Перейти на сайт лабиринт
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.add_cookie(cookie)


    #Найти все книги по слову Python

    browser.find_element(By.CSS_SELECTOR, "input#search-field").send_keys("Python", Keys.RETURN)

    #Переключится на таблицу
    browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div/form/div[1]/div[1]/div/div/span[6]/span/a[2]").click()

    #Добавить все книги в корзину и посчитать сколько их
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located( (By.CSS_SELECTOR, 'table') )
    )
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    print(counter)
    
    #Перейти в корзину
    browser.find_element(By.CSS_SELECTOR, "span.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a").click()
    #Проверить счетчик их должно быть столько сколько раз мы нажали 
    l = browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div/div/div[1]/ul/li[1]/a/b").text
    assert str (counter) == l
    browser.quit()