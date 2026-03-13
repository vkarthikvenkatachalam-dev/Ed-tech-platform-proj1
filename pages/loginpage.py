from pages.basepage import BasePage


class LoginPage(BasePage):
    EMAIL = "#email"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-btn"

    def login(self, email: str, password: str):
        self.wait_for_element(self.EMAIL)
        self.fill_input(self.EMAIL, email)
        self.wait_for_element(self.PASSWORD)
        self.fill_input(self.PASSWORD, password)
        self.click_element(self.LOGIN_BTN)
