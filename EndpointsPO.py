from selenium.webdriver.common.by import By
from BasePage import BasePage

class EndpointPage(BasePage):
    CREATE_NEW_ENDPOINT_BUTTON = (By.XPATH, "//button[contains(text(), 'Create New Endpoint')]")
    SUBMIT_ENDPOINT_BUTTON = (By.XPATH, "//button[contains(text(), 'Create Endpoint')]")

    ENDPOINT_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    ENDPOINT_PATH_INPUT = (By.CSS_SELECTOR, "input[value='/']")
    RESOPONSE_OBJECT_ID_INPUT = (By.CSS_SELECTOR, "input[placeholder='9dcebc0c-1e2e-413c-bee2-dbe1f7dfebe2']")
    ENDPOINT_DELAY_INPUT = (By.CSS_SELECTOR, "input[placeholder='Delay']")

    def refresh_page(self):
        self.refresh_page()
    
    def click_create_new_endpoint_button(self):
        self.click(self.CREATE_NEW_ENDPOINT_BUTTON)
    
    def click_submit_endpoint_button(self):
        self.click(self.SUBMIT_ENDPOINT_BUTTON)
    
    def input_endpoint_name(self, name):
        self.input_text(self.ENDPOINT_NAME_INPUT, name)

    def input_endpoint_path(self, path):
        self.input_text(self.ENDPOINT_PATH_INPUT, path)

    def input_response_object_id(self, response_object_id):
        self.input_text(self.RESOPONSE_OBJECT_ID_INPUT, response_object_id)

    def input_delay(self, delay):
        self.input_text(self.ENDPOINT_DELAY_INPUT, delay)

    def verify_endpoint_creation(self, name: str) -> bool:
        try:
            self.get_text_in_element((By.XPATH, f"//h3[text() = '{name}']"))
            return True
        except Exception:
            return False
        
    def remove_endpont_after_test(self):
        try:
            self.click((By.XPATH, "//button[contains(text(), 'Delete')]"))
        except Exception:
            print("No endpoint found to delete")
        
