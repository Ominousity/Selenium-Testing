from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def find_element(self, by_locator):
        return self.wait_for_element(by_locator)

    def get_text_in_element(self, by_locator):
        return self.find_element(by_locator).text

    def click(self, by_locator):
        self.find_element(by_locator).click()
    
    def input_text(self, by_locator, text):
        self.find_element(by_locator).clear()
        self.find_element(by_locator).send_keys(text)

    def wait_for_element(self, by_locator, timeout=5, poll_frequency=1.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(by_locator))
    
    def refresh_page(self):
        self.driver.refresh()
