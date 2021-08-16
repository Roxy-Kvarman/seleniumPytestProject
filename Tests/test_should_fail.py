from Tests.test_base import TestBase
from Pages.DashboardPage import DashboardPage
import pytest
from Utilities.logger import Logger

class TestShouldFail(TestBase):

    def test_should_fail(self,get_test_name):
        test_name = get_test_name
        Logger.logger.info("----------------------- " + test_name + " -----------------------")

        expected_subject = "Math"

        Logger.logger.info("Navigate to Dashboard Page")
        dashboard_page = DashboardPage()

        Logger.logger.info("Open New Task Page")
        new_task_page = dashboard_page.open_new_task_page()

        Logger.logger.info(f"Verify subject with name: {expected_subject} is in the list")
        is_subject = new_task_page.verify_subject_in_list(expected_subject)
        self.assertTrue(is_subject, f"New Task Page - subject list - subject isn't found in the list. Subject name: {expected_subject}")

        Logger.logger.info("----------------------- finished  -----------------------")

