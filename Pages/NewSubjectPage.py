from Pages.BasePage import BasePage
from Utilities.browser import Browser
from selenium.webdriver.common.by import By
from Utilities.helper import Helper
from Utilities.extensions import Extensions


class NewSubjectPage(BasePage):

    def create_new_subject(self, subject_name):
        name_field = Browser.get_driver().find_element(By.NAME, "name")
        Extensions.insert_text(name_field, subject_name)
        Extensions.click_element((By.XPATH, "//a[text()='Advanced']"))
        Extensions.click_element((By.CSS_SELECTOR, "div.no-dropdown-arrow"))
        year = self._select_random_year()
        rand_color_index = self._select_random_color()
        Extensions.click_element((By.XPATH, "//div[@class='submit']/button[@type='submit']"))
        return rand_color_index, year

    def _select_random_year(self):
        years_list = Browser.get_driver().find_elements(By.XPATH, "//div[@class='v-select-content']/ul/li")
        rand_year_index = Helper.number_generator(len(years_list) - 1)
        year = years_list[rand_year_index].text
        years_list[rand_year_index].click()
        return year

    def _select_random_color(self):
        colors = Browser.get_driver().find_elements(By.XPATH, "//div[@class='menu']/ul/li")
        rand_color_index = Helper.number_generator(len(colors) - 1)
        Extensions.click_element((By.CSS_SELECTOR, "a.menu-btn"))
        color_to_select = colors[rand_color_index]
        color_to_select.click()
        return rand_color_index