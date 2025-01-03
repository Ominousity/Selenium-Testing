from selenium.webdriver.common.by import By
from BasePage import BasePage

class EndpointPage(BasePage):
    CREATE_NEW_ENDPOINT_BUTTON = (By.ID, "create-endpoint-button")
    CREATE_ENDPOINT_BUTTON = (By.ID, "create-endpoint")
    CLOSE_CREATE_ENDPOINT_BUTTON = (By.ID, "close-create-endpoint")

    ENDPOINT_NAME_INPUT = (By.ID, "endpoint-name")
    ENDPOINT_PATH_INPUT = (By.ID, "endpoint-path")
    ENDPOINT_METHOD_SELECT = (By.ID, "endpoint")
    RESOPONSE_OBJECT_ID_INPUT = (By.ID, "response-object-id")
    ENDPOINT_DELAY_INPUT = (By.ID, "endpoint-delay")
