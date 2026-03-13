import re

from pages.basepage import BasePage


class DashboardPage(BasePage):
  PRODUCTS="(//p[text()='Our Products'])[1]"
  LOGOUT_BTN="(//div[@class='⭐️3hk5qd-0 flex items-center gap-3'])[5]/p"

  def logout(self):
      self.wait_for_element(self.PRODUCTS)
      self.page.locator(".⭐️3hk5qd-0.account-box-toggler").first.click()
      print("profile clicked")
      self.page.locator("#account-boxheader").get_by_text("Sign Out")
      print("logout clicked")
