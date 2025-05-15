from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_BUTTON_HEADER = By.XPATH, "//div[contains(@class,'Header_Nav')]/button[contains(text(), 'Заказать')]"
    ORDER_BUTTON_BOTTOM = By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[contains(text(), 'Заказать')]"
    ORDER_PAGE = By.XPATH, "//div[contains(@class, 'Order_Header')]"
    FIELD_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    FIELD_SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    FIELD_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    FIELD_METRO_STATION = By.XPATH, "//input[@placeholder='* Станция метро']"
    BUTTON_DALEE = By.XPATH, "//button[contains(text(), 'Далее')]"
    BUTTON_COOKIE = By.ID, 'rcc-confirm-button'
    FIELD_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    FIELD_RENT_PERIOD = By.CLASS_NAME, 'Dropdown-placeholder'
    FIELD_COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    BUTTON_ZAKAZAT = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(text(), 'Заказать')]"
    BUTTON_CONFIRM = By.XPATH, "//button[contains(text(), 'Да')]"
    CONFIRM_ORDER = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"
    PART_PATH = "//div[contains(text(), '"