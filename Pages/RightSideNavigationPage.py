from Pages.BasePage import BasePage
from Utilities.browser import Browser
from selenium.webdriver.common.by import By
from Utilities.extensions import Extensions
import time
from Pages.SchedulePage import SchedulePage
from Pages.DashboardPage import DashboardPage
from Pages.TasksPage import TasksPage
from Pages.ExamsPage import ExamsPage
from Pages.CalendarPage import CalendarPage
from Pages.SchedulePage import SchedulePage
from Pages.SearchPage import SearchPage


class RightSideNavigationPage(BasePage):

    def get_pages_urls_list_by_link(self):
        urls = []
        links = Browser.get_driver().find_elements(By.CSS_SELECTOR, "nav#views-nav>div>a")
        for link in links:
            link.click()
            url = Browser.get_driver().current_url
            urls.append(url)
        return urls

    @classmethod
    def open_page_by_link(cls, page_name):
        page_names = {"dashboard": DashboardPage(),
                      "calendar": CalendarPage(),
                      "tasks": TasksPage(),
                      "exams": ExamsPage(),
                      "schedule": SchedulePage(),
                      "search": SearchPage()}
        page = None
        for name in page_names:
            if page_name.lower() == name:
                page = page_names.get(name)
                break
        link = Browser.get_driver().find_element(By.XPATH, f"//a[contains(@href,'{page_name.lower()}')]")
        link.click()
        time.sleep(5)
        return page
