from pages.basepage import BasePage


class HomePage(BasePage):
    LOGIN_BTN = "//button[normalize-space()='Login']"
    SIGNUP_BTN = "//button[normalize-space()='Sign up']"
    COURSES = "(//p[text()='Courses'])[1]"
    LIVE_CLASSES = "(//p[text()='LIVE Classes'])[1]"
    PRACTICE = "(//p[text()='Practice'])[1]"
    DOBBY_WIDGET = "//span[@aria-label='Chat Widget']"

    def click_login(self):
        self.wait_for_element(self.LOGIN_BTN)
        self.click_element(self.LOGIN_BTN)

    def click_signup(self):
        self.wait_for_element(self.SIGNUP_BTN)
        self.click_element(self.SIGNUP_BTN)

    def validate_menu_items(self):
        self.wait_for_element(self.COURSES)
        self.wait_for_element(self.LIVE_CLASSES)
        self.wait_for_element(self.PRACTICE)

    def validate_dobby_widget(self):
        self.wait_for_element(self.DOBBY_WIDGET)