from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

driver.get("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.CSS_SELECTOR, "div#shopping_cart_container").click()

driver.find_element(By.CSS_SELECTOR, "button#checkout").click()

driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys("Торхов")
driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys("Алексей")
driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys("61000")
driver.find_element(By.CSS_SELECTOR, "input#continue").click()

price = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
driver.quit()

print(price)

def test_price():
    assert price == "Total: $58.29"
