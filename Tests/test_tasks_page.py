from Tests.test_base import TestBase
import pytest
from Utilities.logger import Logger
from Pages.DashboardPage import DashboardPage
from Utilities.helper import Helper
import time
from Pages.SchedulePage import SchedulePage
from Pages.RightSideNavigationPage import RightSideNavigationPage


class TestTasksPage(TestBase):

    def test_create_task_from_app_bar(self,get_test_name):
        test_name = get_test_name

        Logger.logger.info("----------------------- " + test_name + " -----------------------")
        Logger.logger.info("Open Tasks Page")
        tasks_page = RightSideNavigationPage.open_page_by_link("Tasks")

        Logger.logger.info("Open New Task Page")
        new_task_page = tasks_page.open_new_task_page()

        Logger.logger.info("Create task with random subject, random type and random date")
        deleted_subject = new_task_page.delete_random_subject()

        Logger.logger.info(f"Verify subject: {deleted_subject} is deleted")
        # manage_subjects_page = schedule_page.open_manage_subjects_page()
        # is_deleted = manage_subjects_page.verify_subject_is_displayed(deleted_subject, False)
        # self.assertTrue(is_deleted, f"Failed to delete subject: {deleted_subject}")

        Logger.logger.info("----------------------- finished  -----------------------")
