import allure
import pytest
from selenium import webdriver
from url import TestUrl
from pages.order_page import Order
from data import Data
from locators.order_page_locators import OrderPageLocators


class TestOrder:

    @allure.title('Тест на создание заказа')
    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (OrderPageLocators.ORDER_BUTTON_HEADER, Data.ORDER_DATA_1),
            (OrderPageLocators.ORDER_BUTTON_BOTTOM, Data.ORDER_DATA_2)
        ]
    )
    def test_order(self, driver_firefox, locator, order_data):
        driver_firefox.get(TestUrl.HOMEPAGE_URL)
        order_page = Order(driver_firefox)
        order_page.click_cookie_button()
        order_page.click_to_element(locator)
        order_page.set_order(order_data)
        assert "Заказ оформлен" in order_page.check_order()