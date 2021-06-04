from re import search

from Pages.SecurePage import SecurePage
from Steps.StepLoginPage import StepLoginPage
from TestData.login_test_data import LoginData
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_login_logout(self):
        self.loginPage = StepLoginPage(self.driver)
        self.loginPage.do_login(LoginData.USER_NAME, LoginData.USER_PASSWORD)
        self.securePage = SecurePage(self.driver)
        secure_text = self.securePage.get_message_text()
        assert search(LoginData.SECURE_MESSAGE, secure_text)
        self.securePage.do_logout()
        self.loginPage = StepLoginPage(self.driver)
        assert self.loginPage.get_url() == LoginData.LOGIN_URL

    def test_wrong_login(self):
        self.loginPage = StepLoginPage(self.driver)
        self.loginPage.do_login(LoginData.WRONG_USER_NAME, LoginData.WRONG_USER_PASSWORD)
        alert_text = self.loginPage.get_alert_message()
        assert search(LoginData.ALERT_MESSAGE, alert_text)
