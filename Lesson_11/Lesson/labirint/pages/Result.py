from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Result:

    def __init__(self, driver: WebDriver):
        self._driver = driver



    def table(self):

        self._driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div/form/div[1]/div[1]/div/div/span[6]/span/a[2]").click()


    def add_books(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located( (By.CSS_SELECTOR, 'table') )
        )
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, ".btn.buy-link.btn-primary")
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
        
        return counter  
