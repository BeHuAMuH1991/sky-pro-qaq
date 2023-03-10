from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def screen_shoot(browser):
    browser.get("https://ya.ru")

    browser.save_screenshot('./ya' + browser.name + '.png')
    sleep(3)
    browser.quit()

screen_shoot(chrome)
screen_shoot(ff)





