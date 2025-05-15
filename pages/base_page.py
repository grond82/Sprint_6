from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver_chrome):
        self.driver = driver_chrome

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self,locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def enter_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_not_form, num):
        method, locator = locator_not_form
        locator = locator.format(num)
        return (method, locator)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def format_locator_metro(self, locator, station):
        station_path = locator + station + "')]"
        return station_path

    def format_path(self, locator, value):
        value_path = locator + value + "')]"
        return value_path

    def input_enter(self,locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])