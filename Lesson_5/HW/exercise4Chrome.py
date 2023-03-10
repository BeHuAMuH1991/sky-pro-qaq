from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#зайти на сайт лабиринт
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/dynamicid")

for i in range(1, 4):
    search_input = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

sleep(10)

driver.quit()