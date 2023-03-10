from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

cookie = {
    'name': 'cookie_policy',
    'value': '1'
    }



driver.get("https://labirint.ru")
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(cookies)
driver.refresh()
driver.delete_all_cookies()

driver.refresh()
sleep(10)

driver.quit()