from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Utilities.extensions import Extensions
from Pages.LoginPage import LoginPage
from Pages.DashboardPage import DashboardPage

class WelcomePage(BasePage):

    def navigate_to_login_page(self):
        Extensions.click_element((By.XPATH, "//a[text()='Sign In']"))
        Extensions.wait_for_page_to_load((By.CSS_SELECTOR, "a.btn.light"))
        Extensions.click_element((By.CSS_SELECTOR, "a.btn.light"))
        Extensions.wait_for_page_to_load((By.XPATH, "//section[@class='credentials']"))
        return LoginPage()

    def navigate_to_dashboard_page(self):
        Extensions.click_element((By.XPATH, "//a[text()='Sign In']"))
        Extensions.wait_for_page_to_load((By.XPATH, "//div[@class='header-col today']"))
        return DashboardPage()







