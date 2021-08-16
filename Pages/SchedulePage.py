from Pages.BasePage import BasePage
from Utilities.extensions import Extensions
from selenium.webdriver.common.by import By
from Pages.ManageSubjectsPage import ManageSubjectsPage

class SchedulePage(BasePage):

    def open_manage_subjects_page(self):
        Extensions.click_element((By.XPATH, "//a[text()='Manage Subjects']"))
        Extensions.wait_for_page_to_load((By.ID, "subjects"))
        return ManageSubjectsPage()