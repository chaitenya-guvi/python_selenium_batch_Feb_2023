from selenium import webdriver
from selenium.webdriver.common.by import By

import time


class IMDB_elements:
    # tables - table , tbody , thead - headers of a table  , tr -- rows , td - individual in a table
    def __init__(self):
        self.url = "https://www.imdb.com/search/title/"
        self.driver = webdriver.Chrome()
        self.id_ofTV_episode_checkbox = 'title_type-4'
        self.css_ofTV_episode_checkbox = '#title_type-4'
        self.name_of_genres = 'genres'

    def browse_imdb(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def finding_elements_on_imdb(self):
        # webelement_of_tv_episode_checkbox = self.driver.find_element_by_id(self.id_ofTV_episode_checkbox)
        webelement_of_tv_episode_checkbox = self.driver.find_element(By.ID, self.id_ofTV_episode_checkbox)

        if webelement_of_tv_episode_checkbox:
            print("element found using id")
        else:
            print("element not found using id")

        # webelement_of_tv_episode_checkbox_using_css = self.driver.find_element_by_css_selector(self.css_ofTV_episode_checkbox)
        webelement_of_tv_episode_checkbox_using_css = self.driver.find_element(By.CSS_SELECTOR,
                                                                               self.css_ofTV_episode_checkbox)
        if webelement_of_tv_episode_checkbox_using_css:
            print("element found using css")
        else:
            print("element not found using id")

    def finding_elements_on_imdb_2(self):
        "example of find elements , finding the number of genres "
        # webelements_of_genres = self.driver.find_elements_by_name(self.name_of_genres)
        webelements_of_genres = self.driver.find_elements(By.NAME, self.name_of_genres)
        if webelements_of_genres:
            print(len(webelements_of_genres))
            print("element found using name")
        else:
            print("element not found using name")

        # example of non existent webelements
        # webelements_of_tile_types = self.driver.find_elements_by_name('abc')  # elements with name abc are nonexistent
        webelements_of_tile_types = self.driver.find_elements(By.NAME, 'abc')  # elements with name abc are nonexistent
        if webelements_of_tile_types:
            print("element found using name")
        else:
            print(webelements_of_tile_types)
            print(len(webelements_of_tile_types))
            print("elements not found using name")

    def finding_elements_on_imdb_3(self):
        "example of link text "
        # webelement_using_link_text = self.driver.find_element(By.LINK_TEXT,"Advertising")
        # webelement_using_link_text.click()

        #
        # webelement_using_link_text = self.driver.find_element(By.PARTIAL_LINK_TEXT,"Advert")
        # webelement_using_link_text.click()
        # time.sleep(5)
        #
        # webelement_using_link_text = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "IMDb")
        # print("The elements identified are ")
        # print(len(webelement_using_link_text))
        # time.sleep(5)
        #
        # webelement_using_a_tags = self.driver.find_elements(By.TAG_NAME, "a")
        # print(f"The elements identified with a tags or link tags  are :  {len(webelement_using_a_tags)}")
        # time.sleep(5)
        #
        # webelement_using_img_tags = self.driver.find_elements(By.TAG_NAME, "img")
        # print(f"The number of imagers on the webpage are  :  {len(webelement_using_img_tags)}")
        #

    def finding_elements_on_imdb_4(self):
        """
        example on finding using
        :return:
        """
        webelement_using_class_attribute = self.driver.find_elements(By.CLASS_NAME, "label")
        print(f"The number of labels on the webpage are  :  {len(webelement_using_class_attribute)}")


obj = IMDB_elements()
obj.browse_imdb()
# obj.finding_elements_on_imdb()
# obj.finding_elements_on_imdb_2()
# obj.finding_elements_on_imdb_3()
obj.finding_elements_on_imdb_4()
