from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
#  Explicit waits   --
from selenium.webdriver.support.wait import WebDriverWait
# Expected conditions
from selenium.webdriver.support import expected_conditions as EC
# Exceptions
from selenium.common.exceptions import *


# DRY = Do not repeat yourself
# syntax of xpath = //tagname[@attribute = 'xxxx']
# every function should accomplish only one single task

class OrangeHrm:

    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Chrome()
        self.username = "Admin"
        self.password = "admin123"
        self.username_locator_name_tag = "username"
        # self.username_locator_name_tag ='//input[@name = "username"]'
        self.password_locator_name_tag = "password"
        self.logging_out_menu = '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]'
        self.logging_out = "//a[text()='Logout']"

    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, timeout=20, poll_frequency=1, ignored_exceptions=[InvalidSelectorException,ElementClickInterceptedException, NoSuchElementException])
        self.wait2 = WebDriverWait(self.driver, timeout=20)
        # sleep(5)

    def input_credentials(self):
        try :
            username_webelement = self.driver.find_element(By.NAME, self.username_locator_name_tag)
        except :
            username_webelement = self.wait.until(EC.element_to_be_clickable((By.NAME, self.username_locator_name_tag)))

        username_webelement.send_keys(self.username)

        password_webelement = self.driver.find_element(By.NAME, self.password_locator_name_tag)
        password_webelement.send_keys(self.password)

        # sleep(2)
        #  login button on orange hrm
        login_path_xpath = '//button[@type="submit"]'
        login_button_webelement = self.driver.find_element(By.XPATH, login_path_xpath)
        login_button_webelement.click()
        title_1 = self.driver.title
        print(title_1)

        try :
            logout_menu_webelement = self.driver.find_element(By.XPATH, self.logging_out_menu)
        except :
            logout_menu_webelement = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.logging_out_menu)))

        logout_menu_webelement.click()
        # sleep(3)

        actions_obj = ActionChains(self.driver)
        logout_webelement = self.driver.find_element(By.XPATH, self.logging_out)
        # no Action chain is successfull without perform function
        actions_obj.move_to_element(logout_webelement).perform()
        # sleep(5)


obj = OrangeHrm()
obj.browse()
obj.input_credentials()