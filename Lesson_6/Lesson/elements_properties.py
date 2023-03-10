from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://ya.ru")

usd = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").text
print(usd)

tag = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").tag_name
print(tag)

id = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").id
print(id)

href = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").get_attribute("href")
print(href)

value = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").value_of_css_property("font-family")
print(value)
color = driver.find_element(By.CSS_SELECTOR, "a[title='USD MOEX']").value_of_css_property("color")
print(color) 

""" driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/visibility")

is_displayed = driver.find_element(By.CSS_SELECTOR, "button#transparentButton").is_displayed()
print(is_displayed)
sleep(3)

click_hide = driver.find_element(By.CSS_SELECTOR, "button#hideButton").click()
is_displayed = driver.find_element(By.CSS_SELECTOR, "button#transparentButton").is_displayed()
print(is_displayed) """

""" driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demoqa.com/radio-button")

yes = driver.find_element(By.CSS_SELECTOR, "input#yesRadio").is_enabled()
print(yes)


no = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
print(no) """


""" driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/checkboxes")

check_box = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
is_selected = check_box.is_selected()
print(is_selected)


check_box.click()
is_selected = check_box.is_selected()
print(is_selected) """

""" driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/checkboxes")

div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
 """

sleep(5)
driver.quit