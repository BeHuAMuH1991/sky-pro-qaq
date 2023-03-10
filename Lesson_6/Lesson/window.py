from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https:vk.com")

""" driver.maximize_window()
sleep(3)
driver.minimize_window()
sleep(3)
driver.fullscreen_window()
sleep(3) """
driver.set_window_size(1000, 600) #задать размер
sleep(10)
driver.quit