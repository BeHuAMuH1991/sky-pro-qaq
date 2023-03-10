from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#зайти на сайт лабиринт
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

search_input = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

driver.quit()