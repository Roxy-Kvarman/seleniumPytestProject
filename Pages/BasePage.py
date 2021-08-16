from selenium.webdriver.support.ui import WebDriverWait
from Utilities.browser import Browser
from Utilities.extensions import Extensions
from selenium.webdriver.common.by import By
# from Pages.NewTaskPage import NewTaskPage


class BasePage():

    isLogin = False

    @property
    def page_title(self):
        WebDriverWait(Browser.get_driver(), 5)
        return Browser.get_driver().title

    # def open_new_task_page(self):
    #     Extensions.click_element((By.XPATH, "//a[@class='btn']"))
    #     Extensions.wait_for_page_to_load()
    #     return NewTaskPage()





