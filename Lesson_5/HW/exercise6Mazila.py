from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

#зайти на сайт лабиринт
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(5)
search_input = driver.find_element(By.XPATH, "div.modal-footer").click()
sleep(5)
driver.quit()
