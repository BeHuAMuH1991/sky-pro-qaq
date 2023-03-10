from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#зайти на сайт лабиринт
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

search_input = driver.find_element(By.CSS_SELECTOR, '[class*="btn-primary"]')


i = 0

for i in range(0, 3):
    search_input.send_keys(Keys.RETURN)
    driver.switch_to.alert.accept()
    i = i + 1

print("Нажал на кнопку", i, "раз!")

driver.quit()