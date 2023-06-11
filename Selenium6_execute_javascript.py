from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class Google:
    def __init__(self):
        self.url = "https://www.google.com"
        self.driver = webdriver.Chrome()

    def browse(self):
        self.driver.get(self.url)
        window_size = self.driver.get_window_size()
        print(f"The window size is : + {window_size}")
        # self.driver.maximize_window()
        sleep(5)

    def InputElemnts(self):
        xpath_of_input_element = "//*[@name = 'q']"
        web_element = self.driver.find_element(By.XPATH, xpath_of_input_element)
        web_element.click()
        web_element.send_keys("Guvi")
        web_element.send_keys(Keys.ENTER)
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,660);")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,660);")
        sleep(3)
        # self.driver.execute_script("window.scrollBy(-300,0);")
        # sleep(3)
        # self.driver.execute_script("window.scrollBy(0,200);")
        # sleep(3)
        # self.driver.execute_script("window.scrollBy(0,-200);")
        # sleep(3)


obj = Google()
obj.browse()
obj.InputElemnts()
