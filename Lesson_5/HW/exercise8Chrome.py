from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

#зайти на сайт лабиринт
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/login")

search_input_name = driver.find_element(By.CSS_SELECTOR, "input#username")
search_input_name.send_keys("tomsmith")

search_input_password = driver.find_element(By.CSS_SELECTOR, "input#password")
search_input_password.send_keys("SuperSecretPassword!", Keys.RETURN)

sleep(10)
driver.quit()