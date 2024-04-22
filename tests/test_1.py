import pytest
import allure
from selenium.webdriver.common.by import By

from pages.page import Page
from lib.assertions import Assertions


@allure.feature('Тест набор')
class Test1:

    @allure.title('Тесткейс 1.0')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures("get_driver")
    def test_1(self):
        self.page = Page(self.driver)

        self.page.elements_open()
        self.page.element_check_box_open()
        self.page.home_open()
        self.page.downloads_open()
        self.page.checkbox_click()

        assert self.driver.find_element(By.XPATH, self.page.WORD_FILE_RESULT1)
        assert self.driver.find_element(By.XPATH, self.page.WORD_FILE_RESULT2)
