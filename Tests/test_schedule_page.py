from Tests.test_base import TestBase
import pytest
from Utilities.logger import Logger
from Pages.RightSideNavigationPage import RightSideNavigationPage

class TestSchedulePage(TestBase):

    def test_delete_subject(self,get_test_name):
        test_name = get_test_name
        Logger.logger.info("----------------------- " + test_name + " -----------------------")
        Logger.logger.info("Open Schedule Page")
        schedule_page = RightSideNavigationPage.open_page_by_link("Schedule")

        Logger.logger.info("Open Manage Subjects Page")
        manage_subjects_page = schedule_page.open_manage_subjects_page()

        Logger.logger.info("Delete random subject and return deleted subject name")
        deleted_subject = manage_subjects_page.delete_random_subject()

        Logger.logger.info(f"Verify subject: {deleted_subject} is deleted")
        manage_subjects_page = schedule_page.open_manage_subjects_page()
        is_deleted = manage_subjects_page.verify_subject_is_displayed(deleted_subject, False)
        self.assertTrue(is_deleted, f"Failed to delete subject: {deleted_subject}")

        Logger.logger.info("----------------------- finished  -----------------------")


