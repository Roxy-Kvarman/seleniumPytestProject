from Utilities.browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from Utilities.logger import Logger
import time
from selenium.webdriver.common.action_chains import ActionChains
import random

class Extensions:

    driver = Browser.get_driver()

    @classmethod
    def click_element(cls, locator):
        time.sleep(5)
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @classmethod
    def wait_for_page_to_load(cls, locator=None):
        if locator is not None:
            WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located(locator))
        else:
            WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))

    @classmethod
    def insert_text(cls, element, value):
        element.click()
        element.clear()
        element.send_keys(value)


    @classmethod
    def select_element_by_index(cls, element, index):
        select = Select(element)
        select.select_by_index(index)

    @classmethod
    def select_element_by_name(cls, element, name):
        select = Select(element)
        select.select_by_visible_text(name)

    @classmethod
    def select_random_element_by_name(cls, element, options_list):
        select = Select(element)
        random_element = random.choice(options_list)
        select.select_by_visible_text(random_element.text)

    @classmethod
    def hover_and_click_element(cls, element):
        hover = ActionChains(Browser.get_driver()).move_to_element(element)
        time.sleep(5)
        hover.click().perform()

    @classmethod
    def hover_element(cls, element):
        hover = ActionChains(Browser.get_driver()).move_to_element(element)
        hover.perform()