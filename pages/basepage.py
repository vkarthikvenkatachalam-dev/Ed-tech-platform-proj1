class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url:str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_element(self,selector: str,timeout=10000):
        try:
            self.page.wait_for_selector(selector,timeout=timeout)
        except Exception as e:
            raise AssertionError(f"Element not found: {selector}") from e
    def click_element(self,selector:str):
        self.page.click(selector)

    def fill_input(self,selector:str,text:str):
        self.page.fill(selector,text)

    def get_text(self,selector:str):
        return self.page.inner_text(selector)

    def assert_title_contains(self,expected:str):
        actual = self.page.title()
        assert expected in actual, f"Expected '{expected}' in title, got '{actual}'"

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)