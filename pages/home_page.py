import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class Home_Page(BasePage):

    @allure.step('Прокрутка до вопросов')
    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_question_formatted = self.format_locators(HomePageLocators.QUESTION_LOCATOR, num)
        self.scroll_down()
        self.click_to_element(locator_question_formatted)

    @allure.step('Получение ответа')
    def get_answer_text(self, num):
        locator_answer_formatted = self.format_locators(HomePageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_answer_formatted)

    @allure.step('Полный шаг - клик и получение ответа')
    def click_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)