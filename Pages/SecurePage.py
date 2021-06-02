from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SecurePage(BasePage):
    MESSAGE_ELEMENT = (By.ID, "flash")
    LOGOUT_BUTTON = (By.PARTIAL_LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        self.click_on(self.LOGOUT_BUTTON)

    def get_message_text(self):
        return self.get_text_from(self.MESSAGE_ELEMENT)
