from selenium.webdriver.common.by import By

from Config.config import TestConfig
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    USER_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Login')]")
    ALERT_MSS = (By.ID, "flash")

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(TestConfig.LOGIN_URL)

    def do_login(self, username, password):
        self.write_on_field(self.USER_FIELD, username)
        self.write_on_field(self.PASSWORD_FIELD, password)
        self.click_on(self.LOGIN_BUTTON)
        return self.driver

    def get_alert_text(self):
        return self.get_text_from(self.ALERT_MSS)
