import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class Order(BasePage):

    @allure.step('Клик на куки')
    def click_cookie_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_COOKIE)

    @allure.step('Ввод имени')
    def input_name(self, name):
        self.enter_text_to_element(OrderPageLocators.FIELD_NAME, name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname):
        self.enter_text_to_element(OrderPageLocators.FIELD_SURNAME, surname)

    @allure.step('Ввод адреса')
    def input_address(self, address):
        self.enter_text_to_element(OrderPageLocators.FIELD_ADDRESS, address)

    @allure.step('Ввод телефона')
    def input_phone(self, phone):
        self.enter_text_to_element(OrderPageLocators.FIELD_PHONE, phone)

    @allure.step('Ввод станции метро')
    def click_input_metro_station(self):
        self.click_to_element(OrderPageLocators.FIELD_METRO_STATION)

    def stations_format(self, station):
        station_path = f'//div[contains(text(), \'{station}\')]'
        return station_path

    @allure.step('Ввод станции метро')
    def input_metro_station(self, station):
        station_path = self.stations_format(station)
        path = [By.XPATH, station_path]
        self.click_to_element(OrderPageLocators.FIELD_METRO_STATION)
        self.click_to_element(path)

    @allure.step('Клик на кнопку Далее')
    def click_button_dalee(self):
        self.click_to_element(OrderPageLocators.BUTTON_DALEE)

    @allure.step('Ввод даты')
    def input_date(self, date):
        self.enter_text_to_element(OrderPageLocators.FIELD_DATE, date)
        self.driver.find_element(*OrderPageLocators.FIELD_DATE).send_keys(Keys.ENTER)

    @allure.step('Ввод периода аренды')
    def input_rent_period(self, period):
        self.click_to_element(OrderPageLocators.FIELD_RENT_PERIOD)
        period_path = f'//div[contains(text(), \'{period}\')]'
        path = [By.XPATH, period_path]
        self.click_to_element(path)

    @allure.step('Ввод цвета')
    def input_color(self, color):
        color_path = [By.ID, color]
        self.click_to_element(color_path)

    @allure.step('Ввод коментария')
    def input_comment(self, comment):
        self.enter_text_to_element(OrderPageLocators.FIELD_COMMENT, comment)

    @allure.step('Клик на кнопку заказать')
    def click_button_zakazat(self):
        self.click_to_element(OrderPageLocators.BUTTON_ZAKAZAT)

    @allure.step('Подтвержение аренды')
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.BUTTON_CONFIRM)

    @allure.step('Полный шаг - создать заказ')
    def set_order(self, order_data):
        self.input_name(order_data.get('name'))
        self.input_surname(order_data.get('surname'))
        self.input_address(order_data.get('address'))
        self.input_metro_station(order_data.get('metro_station'))
        self.input_phone(order_data.get('phone'))
        self.click_button_dalee()
        self.input_date(order_data.get('date'))
        self.input_rent_period(order_data.get('rent_period'))
        self.input_color(order_data.get('color'))
        self.input_comment(order_data.get('comment'))
        self.click_button_zakazat()
        self.confirm_order()