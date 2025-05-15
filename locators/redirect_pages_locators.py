from selenium.webdriver.common.by import By

class RedirectPageLocators:
    LOGO_SAMOKAT = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
    LOCATOR_FOR_TEST_REDIRECT_LOGO_SAMOKAT = By.XPATH, "//div[contains(@class, 'Home_Header')]"
    NEWS = By.XPATH, "//div[contains(@class, 'dzen-desktop--floor-title')]"