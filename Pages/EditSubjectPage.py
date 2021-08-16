from Utilities.extensions import Extensions
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Utilities.browser import Browser


class EditSubjectPage(BasePage):

    def delete_subject(self):
        delete_button = Browser.get_driver().find_element(By.XPATH, "//a[contains(@class,'delete')]")
        Extensions.hover_and_click_element(delete_button)
        Extensions.click_element((By.XPATH, "//a[contains(@ng-click,'confirm')]"))

