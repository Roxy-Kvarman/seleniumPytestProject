from Pages.BasePage import BasePage
from Utilities.extensions import Extensions
from selenium.webdriver.common.by import By
from Pages.NewTaskPage import NewTaskPage
import time
from Utilities.browser import Browser

class DashboardPage(BasePage):

    def open_new_task_page(self):
        Extensions.click_element((By.XPATH, "//a[@class='btn']"))
        Extensions.wait_for_page_to_load()
        return NewTaskPage()


    def get_tasks_count(self,):
        tasks_count = Browser.get_driver().find_element(By.XPATH, "//div[@class='header-col tasks']")
        count = int(tasks_count.text.split()[3])
        return count

