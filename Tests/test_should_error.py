from Tests.test_base import TestBase
from Pages.DashboardPage import DashboardPage
import pytest
from Utilities.logger import Logger


class TestShouldError(TestBase):
    @pytest.mark.sanity
    def test_should_error(self,get_test_name):
        test_name = get_test_name
        Logger.logger.info("----------------------- " + test_name + " -----------------------")

        index = -1
        Logger.logger.info("Navigate to Dashboard Page")
        dashboard_page = DashboardPage()

        Logger.logger.info("Get tasks count before adding new task")
        tasks_count_before = dashboard_page.get_tasks_count()

        Logger.logger.info("Add new task")
        new_task_page = dashboard_page.open_new_task_page()
        new_task_page.select_subject_by_index(index)

        Logger.logger.info("Cancel new task")
        new_task_page.cancel_new_task()

        Logger.logger.info("Get tasks count after cancel new task")
        tasks_count_after = dashboard_page.get_tasks_count()

        Logger.logger.info("Verify tasks count doesn't change")
        self.assertEqual(tasks_count_before, tasks_count_after, "New task was created though it was cancelled")

        Logger.logger.info("----------------------- finished  -----------------------")



