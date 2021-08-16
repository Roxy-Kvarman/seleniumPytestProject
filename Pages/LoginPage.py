from Pages.BasePage import BasePage
from Utilities.extensions import Extensions
from selenium.webdriver.common.by import By
from Pages.DashboardPage import DashboardPage
from Utilities.browser import Browser


class LoginPage(BasePage):

    def login(self, username, password):
        field_email = Browser.get_driver().find_element(By.XPATH, "//input[@name='email']")
        field_password = Browser.get_driver().find_element(By.XPATH, "//input[@name='password']")
        Extensions.insert_text(field_email, username)
        Extensions.insert_text(field_password, password)
        Extensions.click_element((By.XPATH, "//button[@type='submit']"))
        Extensions.wait_for_page_to_load()
        return DashboardPage()