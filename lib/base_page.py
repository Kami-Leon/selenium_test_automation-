import time
import allure
from allure_commons.types import AttachmentType


class BasePage:

    driver = None

    def __init__(self, driver):
        self.driver = driver
    
    @staticmethod
    def take_screenshot(self):
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
