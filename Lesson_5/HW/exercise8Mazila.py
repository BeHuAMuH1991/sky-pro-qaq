from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

search_input_name = driver.find_element(By.CSS_SELECTOR, "input#username")
search_input_name.send_keys("tomsmith")

search_input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
search_input_password.send_keys("SuperSecretPassword!", Keys.RETURN)

sleep(10)
driver.quit()