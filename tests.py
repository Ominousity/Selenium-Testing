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

    test_cases_success = [
        ("case_1", "endpoint_name", "path", "645bb1d8-48d5-463b-a2a2-87b7c9e8b9e4", "5"),    # All fields filled
        ("case_2", "endpoint_name", "path", "", "5"),                                        # Empty response object id
    ]

    @parameterized.expand(test_cases_success)
    def test_create_endpoint_succesfully(self, test_name, name: str, path: str, response_object_id: str, delay: int):
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
        assert self.endpoints_page.verify_endpoint_creation(name) == True

    test_cases_failure = [
        ("case_1", "", "path", "645bb1d8-48d5-463b-a2a2-87b7c9e8b9e4", "5"),               # Empty name
        ("case_2", "endpoint_name", "", "645bb1d8-48d5-463b-a2a2-87b7c9e8b9e4", "5"),      # Empty path
        ("case_3", "endpoint_name", "path", "645bb1d848d5463ba2a287b7c9e8b9e4", "5"),      # Malformed GUID
        ("case_4", "endpoint_name", "path", "645bb1d8-48d5-463b-a2a2-87b7c9e8b9e4", ""),   # Empty delay
    ]

    @parameterized.expand(test_cases_failure)
    def test_create_endpoint_failed(self, test_name, name: str, path: str, response_object_id: str, delay: int):
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

        # assert to verify failed creation of endpoint
        assert self.endpoints_page.verify_endpoint_creation(name) == False

    def tearDown(self):
        self.endpoints_page.remove_endpont_after_test()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()