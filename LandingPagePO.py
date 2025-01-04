from selenium.webdriver.common.by import By
from BasePage import BasePage

class LandingPage(BasePage):
    ENDPOINTS_PAGE_BUTTON = (By.LINK_TEXT, "Endpoints")

    def navigate_to_endpoints_page(self):
        self.click(self.ENDPOINTS_PAGE_BUTTON)