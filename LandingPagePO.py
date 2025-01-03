from selenium.webdriver.common.by import By
from BasePage import BasePage

class LandingPage(BasePage):
    ENDPOINTS_PAGE_BUTTON = (By.CSS_SELECTOR, "li.group\/menu-item:nth-child(1)")
    DATA_PAGE_BUTTON = (By.ID, "response-objects-page-button")
    SETTINGS_PAGE_BUTTON = (By.ID, "settings-page-button")

    def navigate_to_endpoints_page(self):
        self.click(self.ENDPOINTS_PAGE_BUTTON)

    def navigate_to_data_page(self):
        self.click(self.DATA_PAGE_BUTTON)

    def navigate_to_settings_page(self):
        self.click(self.SETTINGS_PAGE_BUTTON)