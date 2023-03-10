from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#зайти на сайт лабиринт
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#Нажимаем 5 раз на кнопку
search_input = driver.find_element(By.CSS_SELECTOR, "button")
for i in range(0, 5):
    search_input.send_keys(Keys.RETURN)

#Посчитать сколько раз нажали на кнопку и вывести на экран
clicks = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
print("Количество Delete:", len(clicks))

sleep(5)

driver.quit()