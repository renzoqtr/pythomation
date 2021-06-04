from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_URL = "https://the-internet.herokuapp.com/login"
    USER_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Login')]")
    ALERT_MSS = (By.ID, "flash")

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)

    def write_on_username_field(self, username):
        self.write_on_field(self.USER_FIELD, username)

    def write_on_password_field(self, password):
        self.write_on_field(self.PASSWORD_FIELD, password)

    def click_on_login_button(self):
        self.click_on(self.LOGIN_BUTTON)

    def get_alert_text(self):
        return self.get_text_from(self.ALERT_MSS)
