from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Utilities.extensions import Extensions
from Utilities.browser import Browser
from Utilities.helper import Helper
from Pages.EditSubjectPage import EditSubjectPage
import random

class ManageSubjectsPage(BasePage):

    def delete_random_subject(self):
        subjects_list = self._get_subjects_list()
        rand_subject = random.choice(subjects_list)
        subject_name = rand_subject.text
        rand_subject.click()
        Extensions.wait_for_page_to_load((By.ID, "subject-input"))
        edit_subject_page = EditSubjectPage()
        edit_subject_page.delete_subject()
        self.close_manage_subjects_page()
        return subject_name

    def close_manage_subjects_page(self):
        Extensions.click_element((By.XPATH, "//a[@class='close']"))

    def verify_subject_is_displayed(self, subject_name, should_be_displayed):
        subjects_list = self._get_subjects_list()
        is_displayed = any(x for x in subjects_list if x.text == subject_name)
        return is_displayed == should_be_displayed

    def _get_subjects_list(self):
        Browser.get_driver().execute_script("window.scrollBy(0, 250)", "");
        subjects_list = Browser.get_driver().find_elements(By.XPATH, "//div[contains(@class,'list-inner')]/ul/li/a")
        return subjects_list