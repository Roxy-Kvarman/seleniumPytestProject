import os

from Tests.test_base import TestBase
import pytest
from Utilities.logger import Logger
from Pages.DashboardPage import DashboardPage
from Utilities.helper import Helper
import time


class TestDashboardPage(TestBase):

    def test_create_new_subject(self,get_test_name):
        test_name = get_test_name
        Logger.logger.info("----------------------- " + test_name + " -----------------------")

        subject_name = "subject_" + Helper.string_generator(5)

        Logger.logger.info("Navigate to Dashboard Page")
        dashboard_page = DashboardPage()

        Logger.logger.info("Open New Task Page")
        new_task_page = dashboard_page.open_new_task_page()

        Logger.logger.info("Open New Subject Page")
        new_subject_page = new_task_page.open_new_subject_page()

        Logger.logger.info(f"Create new subject: {subject_name}")
        color_index, year = new_subject_page.create_new_subject(subject_name)
        time.sleep(5)

        Logger.logger.info("Verify new subject is created and selected")
        is_created = new_task_page.verify_subject_in_list(subject_name)
        is_selected = new_task_page.verify_new_subject_is_selected_after_creation(subject_name, color_index, year)
        assert is_created == True and is_selected == True, f"Failed to create and select new subject: {subject_name} with color: {color_index} and academic year: {year}"

        Logger.logger.info("----------------------- finished  -----------------------")






