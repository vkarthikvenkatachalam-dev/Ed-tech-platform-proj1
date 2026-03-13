import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="edge",
        help="Browser to run tests on: edge, chrome, firefox, webkit"
    )

@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("--browser-name")
    with sync_playwright() as p:
        if browser_name == "edge":
            browser = p.chromium.launch(
                channel="msedge",
                headless=False,
                args=["--disable-blink-features=AutomationControlled"]
            )
        elif browser_name == "chrome":
            browser = p.chromium.launch(
                headless=False,
                args=["--disable-blink-features=AutomationControlled"]
            )
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 720},
        locale="en-US"
    )
    page = context.new_page()
    yield page
    context.close()