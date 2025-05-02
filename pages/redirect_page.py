import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.redirect_pages_locators import RedirectPageLocators
from pages.base_page import BasePage

class Redirect(BasePage):

    @allure.step('Клик на лого Самокат')
    def click_logo_samokat(self):
        self.click_to_element(RedirectPageLocators.LOGO_SAMOKAT)

    @allure.step('Клик на лого Яндекс')
    def click_logo_yandex(self):
        self.click_to_element(RedirectPageLocators.LOGO_YANDEX)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(RedirectPageLocators.NEWS))