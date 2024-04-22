import allure
from selenium.webdriver.common.by import By

from lib.base_page import BasePage
from locators.page_locators import PageLocators


class Page(BasePage, PageLocators):

    @allure.step('Нажать кнопку Elements')
    def elements_open(self):
        self.driver.find_element(By.XPATH, PageLocators.ELEMENTS_BUTTON).click()
        self.take_screenshot(self)


    @allure.step('Выбрать элемент Check Box')
    def element_check_box_open(self):
        self.driver.find_element(By.XPATH, PageLocators.CHECK_BOX_BUTTON).click()
        self.take_screenshot(self)


    @allure.step('Раскрыть директорию Home')
    def home_open(self):
        self.driver.find_element(By.XPATH, PageLocators.HOME_BUTTON).click()
        self.take_screenshot(self)


    @allure.step('Раскрыть директорию Downloads')
    def downloads_open(self):
        self.driver.find_elements(By.XPATH, PageLocators.DOWNLOADS_BUTTON)[3].click()
        self.take_screenshot(self)


    @allure.step('Выбрать чекбокс Word File.doc')
    def checkbox_click(self):
        self.driver.find_elements(By.XPATH, PageLocators.CHECK_BOX)[4].click()
        self.take_screenshot(self)
        