from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#зайти на сайт лабиринт
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.labirint.ru/")

#найти книги по слову Python
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys("Python", Keys.RETURN)

#собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product")

#Вывести в консоль информацию(название, автор, цена)
for book in books:
    author = " "
    title = book.find_element(By.CSS_SELECTOR, "span.product-title").text
    price = book.find_element(By.CSS_SELECTOR, "span.price-val").text
    try:
        author = book.find_element(By.CSS_SELECTOR, ".product-author").text
    except:
        author = "Автор не указан"
    print("Автор:", author)
    print("Название:", title)
    print("Цена:", price)
    

sleep(10)   