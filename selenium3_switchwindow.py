from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

"""
switching windows 
a tags are for links 
"""


class Cowin:

    def __init__(self):
        self.url = "https://www.cowin.gov.in/"
        self.driver = webdriver.Chrome()
        self.FAQ_LINK_xpath = "//a[@href='/faq']"

    def browsecowin(self):
        """
        browse cowin page
        :return: None
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(1)

    def browseFAQpage(self):
        """
        Clicking on the FAQ page url
        :return:
        """
        # prints the current URL and saves the current window id
        print("The current URL is : " + self.driver.current_url)
        present_window_handle = self.driver.current_window_handle
        print("Line 35 ----The current handle is : " + present_window_handle)

        # Clicking on faq page
        FAQ_webelement = self.driver.find_element(By.XPATH, self.FAQ_LINK_xpath)
        FAQ_webelement.click()

        # get all the active / availbale window handle
        all_window_handles = self.driver.window_handles
        print("Line 43 ---- Thelist of all windows is : ")
        print(all_window_handles)
        #
        for window_tab_code in all_window_handles:
            if (window_tab_code != present_window_handle):
                self.driver.switch_to.window(window_tab_code)
                sleep(10)
                print("The current URL after clicking is : " + self.driver.current_url)
                # self.driver.close()
                self.driver.quit()

                break  #closes the current window
        #


obj = Cowin()
obj.browsecowin()
obj.browseFAQpage()
