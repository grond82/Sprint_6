import allure
import pytest
from selenium import webdriver
from url import TestUrl
from pages.home_page import Home_Page
from data import Data


class TestImportantQuestions:

    @allure.title('Тест на проверку вопросов')
    @pytest.mark.parametrize(
        'num',
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7
        ]
    )
    def test_question_and_answers(self, driver_chrome, num):
        driver_chrome.get(TestUrl.HOMEPAGE_URL)
        home_page = Home_Page(driver_chrome)
        answer = home_page.click_question_and_answer(num)
        assert answer == Data.ANSWERS_DATA[num]