from re import search

from Config.config import TestConfig

from Pages.SecurePage import SecurePage
from Steps.StepLoginPage import StepLoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_login_logout(self):
        self.loginPage = StepLoginPage(self.driver)
        self.loginPage.do_login(TestConfig.USER_NAME, TestConfig.USER_PASSWORD)
        self.securePage = SecurePage(self.driver)
        secure_text = self.securePage.get_message_text()
        assert search(TestConfig.SECURE_MESSAGE, secure_text)
        self.securePage.do_logout()
        self.loginPage = StepLoginPage(self.driver)
        assert self.loginPage.get_url() == TestConfig.LOGIN_URL

    def test_wrong_login(self):
        self.loginPage = StepLoginPage(self.driver)
        self.loginPage.do_login(TestConfig.WRONG_USER_NAME, TestConfig.WRONG_USER_PASSWORD)
        alert_text = self.loginPage.get_alert_message()
        assert search(TestConfig.ALERT_MESSAGE, alert_text)
