from selenium.webdriver.support import expected_conditions as exc
from selenium.webdriver.support.ui import WebDriverWait

"""This class is the parent page of pages """
""" contains generic methods and utilities"""


class BasePage:
    MAX_WAIT_TIMEOUT = 15

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def click_on(self, by_locator):
        WebDriverWait(self.driver, self.MAX_WAIT_TIMEOUT) \
            .until(exc.element_to_be_clickable(by_locator)) \
            .click()

    def write_on_field(self, field_locator, text):
        field = WebDriverWait(self.driver, self.MAX_WAIT_TIMEOUT) \
            .until(exc.element_to_be_clickable(field_locator))
        field.clear()
        field.send_keys(text)

    def get_text_from(self, by_locator):
        return WebDriverWait(self.driver, self.MAX_WAIT_TIMEOUT) \
            .until(exc.visibility_of_element_located(by_locator)) \
            .text
