from Pages.LoginPage import LoginPage


class StepLoginPage:

    def __init__(self, driver):
        self.loginPage = LoginPage(driver)

    def get_url(self):
        return self.loginPage.get_current_url()

    def do_login(self, username, password):
        self.loginPage.open_login_page()
        self.loginPage.write_on_username_field(username)
        self.loginPage.write_on_password_field(password)
        self.loginPage.click_on_login_button()

    def get_alert_message(self):
        return self.loginPage.get_alert_text()
