import unittest
from selenium import webdriver
from LandingPagePO import LandingPage

class CreateEndpointTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('localhost:5173')
        self.landing_page = LandingPage(self.driver)

    def test_create_endpoint(self):
        self.landing_page.wait_for_element(self.landing_page.ENDPOINTS_PAGE_BUTTON)
        self.landing_page.navigate_to_endpoints_page()

        # Add assertions to verify successful login

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()