import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ImdbSelectExample:
    # tables - table , tbody , thead - headers of a table  , tr -- rows , td - individual in a table
    def __init__(self):
        self.url = "https://www.imdb.com/search/title/"
        self.driver = webdriver.Chrome()

    def browse_imdb(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def select_example(self):
        xpath_for_user_rating = "//select[@name='user_rating-min']"
        webelement_for_select_object = self.driver.find_element(By.XPATH, xpath_for_user_rating)
        select_obj_for_user_rating = Select(webelement_for_select_object)
        select_obj_for_user_rating.select_by_visible_text("1.4")
        time.sleep(5)

    def select_by_value_example(self):
        xpath_for_title_data = "//select[@name='has']"
        webelement_for_select_title_data = self.driver.find_element(By.XPATH, xpath_for_title_data)
        # pass the webelement to select object for initializing
        select_object_for_title_data = Select(webelement_for_select_title_data)
        select_object_for_title_data.select_by_value("plot")
        time.sleep(5)

    def select_by_index_example(self):
        xpath_for_title_data = "//select[@name='has']"
        webelement_for_select_title_data = self.driver.find_element(By.XPATH, xpath_for_title_data)
        # pass the webelement to select object for initializing
        select_object_for_title_data = Select(webelement_for_select_title_data)
        select_object_for_title_data.select_by_index(1)
        time.sleep(5)
        print(f"The options available to title data are : {len(select_object_for_title_data.options)}")
        for index_of_option, element_in_options in enumerate(select_object_for_title_data.options):
            print(f"The value at ,index {index_of_option} in list is  : {element_in_options.text}")


obj = ImdbSelectExample()
obj.browse_imdb()
# obj.select_example()

# obj.select_by_value_example()
obj.select_by_index_example()
