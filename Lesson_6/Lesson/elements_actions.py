from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

element = driver.find_element(By.CSS_SELECTOR, ".search3__input.mini-suggest__input")
element.clear() #очистить элемент
element.send_keys("Привет какшка!") #добавить надпись
sleep(2)
clickss = driver.find_element(By.CSS_SELECTOR, ".search3__button.mini-suggest__button")
clickss.click()

sleep(10)
driver.quit