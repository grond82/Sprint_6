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
        self.switch_window()
        self.find_element_with_wait(RedirectPageLocators.NEWS)

    @allure.step('Проверка редиректа - лого Самокат')
    def check_redirect_logo_samokat(self):
        text = self.get_text_from_element(RedirectPageLocators.LOCATOR_FOR_TEST_REDIRECT_LOGO_SAMOKAT)
        return text

    @allure.step('Проверка редиректа - лого Яндекс')
    def check_redirect_logo_yandex(self):
        text = self.get_text_from_element(RedirectPageLocators.NEWS)
        return text