import re

from playwright.sync_api import expect

from pages.dashboard import DashboardPage
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from test_data import BASE_URL, EXPECTED_TITLE, SIGNIN_URL, VALID_EMAIL, VALID_PASSWORD, INVALID_EMAIL, INVALID_PASSWORD


def test_tc01_url_validity(page):
    home = HomePage(page)
    home.goto(BASE_URL)
    expect(page).to_have_url(re.compile(r"guvi.in"))

def test_tc02_title_check(page):
    home = HomePage(page)
    home.goto(BASE_URL)
    expect(page).to_have_title(EXPECTED_TITLE)

def test_tc03_login_button(page):
    home = HomePage(page)
    home.goto(BASE_URL)
    home.click_login()
    expect(page).to_have_url(re.compile(r"sign-in/"))

def test_tc04_signup_button(page):
    home = HomePage(page)
    home.goto(BASE_URL)
    home.click_signup()
    expect(page).to_have_url(re.compile(r"register/"))

def test_tc05_signup_navigation(page):
    home = HomePage(page)
    home.goto(BASE_URL)
    home.click_signup()
    expect(page).to_have_url(re.compile(r"register/"))

def test_tc06_valid_login(page):
    login = LoginPage(page)
    login.goto(SIGNIN_URL)
    login.login(VALID_EMAIL, VALID_PASSWORD)
    expect(page).to_have_url(re.compile(r"guvi.in"))

def test_tc07_invalid_login(page):
    login = LoginPage(page)
    login.goto(SIGNIN_URL)
    login.login(INVALID_EMAIL, INVALID_PASSWORD)
    assert page.locator("//div[contains(@class,'invalid-feedback')]").count() > 0, "Error message not displayed"


def test_tc08_menu_items(page):
    home = HomePage(page)
    home.goto(BASE_URL)
    home.validate_menu_items()
    expect(page.locator(HomePage.COURSES)).to_be_visible()
    expect(page.locator(HomePage.LIVE_CLASSES)).to_be_visible()
    expect(page.locator(HomePage.PRACTICE)).to_be_visible()

def test_tc09_dobby_assistant(page):
    home = HomePage(page)
    home.goto(BASE_URL)
    home.validate_dobby_widget()
    expect(page.locator(HomePage.DOBBY_WIDGET)).to_be_visible()

def test_tc10_logout(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    login.goto(SIGNIN_URL)
    login.login(VALID_EMAIL, VALID_PASSWORD)
    expect(page.locator(DashboardPage.PRODUCTS)).to_be_visible()
    dashboard.logout()
    expect(page).to_have_url(BASE_URL)