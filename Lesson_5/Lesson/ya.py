from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

sleep(5)


driver.get("https://ya.ru")
sleep(5)
driver.fullscreen_window()
driver.save_screenshot('./ya.png')
sleep(10)




#driver.back() кнопка назад
#driver.forward()  кнопка вперед
#driver.refresh() обновить страницу
#driver.set_window_size(640, 480) установить размер окна