from Pages.BasePage import BasePage
from Utilities.extensions import Extensions
from selenium.webdriver.common.by import By
from Utilities.browser import Browser
from Pages.NewSubjectPage import NewSubjectPage
import random

class NewTaskPage(BasePage):

    def verify_subject_in_list(self, name):
        select = Browser.get_driver().find_element(By.XPATH, "//select[@name='subject']")
        options = select.find_elements_by_tag_name("option")
        is_subject = any(x for x in options if x.text == name)
        return is_subject

    def select_subject_by_name(self, subject):
        select = Browser.get_driver().find_element(By.XPATH, "//select[@name='subject']")
        Extensions.select_element_by_name(select, subject)

    def select_subject_by_index(self, index):
        select = Browser.get_driver().find_element(By.XPATH, "//select[@name='subject']")
        Extensions.select_element_by_index(select, index)

    def cancel_new_task(self):
        Extensions.click_element((By.XPATH, "//button[@type='button']"))

    def open_new_subject_page(self):
        Extensions.click_element((By.CSS_SELECTOR, "a.add-on"))
        Extensions.wait_for_page_to_load((By.XPATH, "//p[text()='New Subject']"))
        return NewSubjectPage()

    def verify_new_subject_is_selected_after_creation(self, subject_name, color_index, year):
        is_selected = False
        is_year = self._is_year_selected(year)
        is_subject = self._is_subject_selected(subject_name)
        task_color = Browser.get_driver().find_elements(By.XPATH, f"//header[contains(@class,'bg-color{color_index}')]")
        if is_subject and is_year and len(task_color) > 0:
            is_selected = True
        return is_selected

    def create_task(self):
        #select random subject from list
        select = Browser.get_driver().find_element(By.XPATH, "//select[@name='subject']")
        options = select.find_elements_by_tag_name("option")
        Extensions.select_random_element_by_name(select, options)

        #select random type
        select = Browser.get_driver().find_element(By.XPATH, "//select[@name='type']")
        options = select.find_elements_by_tag_name("option")
        Extensions.select_random_element_by_name(select, options)

        #select random date
        days_list = []
        Extensions.click_element((By.XPATH, "//div[@class='pikaday']/span"))
        opened_calendar = Browser.get_driver().find_elements(By.XPATH, "//div[@class='pika-single is-bound bottom']")
        if len(opened_calendar) > 0:
            calendar_table = Browser.get_driver().find_element(By.XPATH, "//div[@class='pika-lendar']/table/tbody")
            table_rows = calendar_table.find_elements(By.TAG_NAME, "tr")
            for row in table_rows:
                row_cells = row.find_elements(By.TAG_NAME, "td")
                for cell in row_cells:
                    if cell.get_attribute("class") == "is-today is-selected":
                        cell_index = row_cells.index(cell)
                        cells = row_cells[cell_index:]
                        for c in cells:
                            if c.get_attribute("class") != "empty":
                                days_list.append(c)
        random_date = random.choice(days_list)
        random_date.click()




    def _is_year_selected(self, year):
        selected_year = Browser.get_driver().find_element(By.XPATH, "//p[contains(@class,'subtitle')]").text
        if year == 'None':
            is_year = selected_year == 'No year/term'
        else:
            is_year = selected_year == year
        return is_year

    def _is_subject_selected(self, subject_name):
        is_subject = False
        select = Browser.get_driver().find_element(By.XPATH, "//select[@name='subject']")
        options = select.find_elements_by_tag_name("option")
        for option in options:
            if option.text == subject_name:
                is_subject = option.get_attribute("selected")
                break
        return is_subject

