from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def find_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def wait_for_element(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locator))
