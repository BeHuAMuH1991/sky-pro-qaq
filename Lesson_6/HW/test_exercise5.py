from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 46)
  
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

driver.find_element(By.CSS_SELECTOR, "input#delay").clear()
driver.find_element(By.CSS_SELECTOR, "input#delay").send_keys("4")
driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[1]").click()
driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[4]").click()
driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[2]").click()
driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[15]").click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
)

fifteen = driver.find_element(By.CSS_SELECTOR, "div.screen").text

driver.quit()


def test_fifteen():
    assert fifteen == "15"