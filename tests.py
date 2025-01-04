import unittest
from parameterized import parameterized
from selenium import webdriver
from LandingPagePO import LandingPage
from EndpointsPO import EndpointPage

class CreateEndpointTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('localhost:5173')
        self.landing_page = LandingPage(self.driver)
        self.endpoints_page = EndpointPage(self.driver)

    test_cases = [
        ("test_case_1", "test_case_1", "645bb1d8-48d5-463b-a2a2-87b7c9e8b9e4", "5"),
        #("", "test_case_2", "645bb1d8-48d5-463b-a2a2-87b7c9e8b9e4", "5"),
        #("test_case_3", "", "645bb1d8-48d5-463b-a2a2-87b7c9e8b9e4", "5"),
        #("test_case_4", "test_case_4", "", "5"),
        #("test_case_5", "test_case_5", "645bb1d8-48d5-463b-a2a2-87b7c9e8b9e4", ""),
    ]

    @parameterized.expand(test_cases)
    def test_create_endpoint(self, name: str, path: str, response_object_id: str, delay: int):
        # Navigate to endpoints page
        self.landing_page.navigate_to_endpoints_page()

        # Click on create endpoint
        self.endpoints_page.click_create_new_endpoint_button()

        # Fill in endpoint details
        self.endpoints_page.input_endpoint_name(name)
        self.endpoints_page.input_endpoint_path(path)
        self.endpoints_page.input_response_object_id(response_object_id)
        self.endpoints_page.input_delay(delay)

        # Click on submit button
        self.endpoints_page.click_submit_endpoint_button()

        # Refresh page to get the updated list of endpoints
        self.driver.refresh()

        # assert to verify successful creation of endpoint
        assert self.endpoints_page.find_name_in_endpoints(name)

    #def tearDown(self):
    #    self.driver.quit()

if __name__ == '__main__':
    unittest.main()