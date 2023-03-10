from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

#зайти на сайт лабиринт
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("1000", Keys.RETURN)
sleep(2)
search_input.clear()
search_input.send_keys("1111", Keys.RETURN)

sleep(5)
driver.quit()