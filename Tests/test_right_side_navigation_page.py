import os

import pytest

from Tests.conftest import get_test_name
from Tests.test_base import TestBase
from Utilities.logger import Logger
from Pages.RightSideNavigationPage import RightSideNavigationPage


class TestRightSideNavigationPage(TestBase):


    def test_verify_pages_urls(self,get_test_name):
        test_name = get_test_name
        Logger.logger.info("----------------------- " + test_name + " -----------------------")
        expected_urls_list = [
            "https://app.mystudylife.com/dashboard",
            "https://app.mystudylife.com/calendar",
            "https://app.mystudylife.com/tasks",
            "https://app.mystudylife.com/exams",
            "https://app.mystudylife.com/schedule",
            "https://app.mystudylife.com/search"
        ]
        Logger.logger.info("Navigate to Right Side Navigation Page")
        right_side_navigation_page = RightSideNavigationPage()

        Logger.logger.info("Get url of each page link by clicking on its icon")
        actual_urls_list = right_side_navigation_page.get_pages_urls_list_by_link()

        Logger.logger.info("Verify expected and actual list of page urls")
        assert expected_urls_list == actual_urls_list, f"Actual pages urls list isn't equal to expected urls list"



        Logger.logger.info("----------------------- finished  -----------------------")


