from re import search

from Config.config import TestConfig
from Pages.LoginPage import LoginPage
from Pages.SecurePage import SecurePage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_login_logout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.open_login_page()
        self.securePage = SecurePage(
            self.loginPage.do_login(TestConfig.USER_NAME, TestConfig.USER_PASSWORD)
        )
        secure_text = self.securePage.get_message_text()
        assert search(TestConfig.SECURE_MESSAGE, secure_text)
        self.loginPage = LoginPage(self.securePage.do_logout())
        assert self.loginPage.get_current_url() == TestConfig.LOGIN_URL

    def test_wrong_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.open_login_page()
        self.loginPage.do_login(TestConfig.WRONG_USER_NAME, TestConfig.WRONG_USER_PASSWORD)
        alert_text = self.loginPage.get_alert_text()
        assert search(TestConfig.ALERT_MESSAGE, alert_text)
