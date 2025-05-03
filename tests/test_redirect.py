import allure
import pytest
from selenium import webdriver
from url import TestUrl
from pages.redirect_page import Redirect
from locators.redirect_pages_locators import RedirectPageLocators


class TestRedirect():

    @allure.title('Тест на редирект - лого Самокат')
    def test_redirect_logo_samokat(self, driver_firefox):
        driver_firefox.get(TestUrl.ORDERPAGE_URL)
        redirect_page = Redirect(driver_firefox)
        redirect_page.click_logo_samokat()
        assert "на пару дней" in redirect_page.check_redirect_logo_samokat()

    @allure.title('Тест на редирект - лого Яндекс')
    def test_redirect_logo_yandex(self, driver_firefox):
        driver_firefox.get(TestUrl.HOMEPAGE_URL)
        redirect_page = Redirect(driver_firefox)
        redirect_page.click_logo_yandex()
        assert redirect_page.check_redirect_logo_yandex() == "Новости"