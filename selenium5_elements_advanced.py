from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.service import Service
from time import sleep

from Locators_LetsKodeit_practcePage import PracticePage


class Test1:
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def __init__(self):
        self.driver = webdriver.Chrome()
        # service=Service(ChromeDriverManager().install()))
        self.url = "https://www.letskodeit.com/practice"

    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(4)
        webelement_benz_using_relative = self.driver.find_element(By.ID, PracticePage().id_of_BMW_checkbox)
        webelement_benz_using_absolute = self.driver.find_element(By.XPATH, PracticePage().absolute_xpath_ofBenz)
        # Action
        webelement_benz_using_absolute.click()

        sleep(5)
        webelement_benz_using_relative.click()
        sleep(5)


Test1().browse()

