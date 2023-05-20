from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


# DRY = Do not repeat yourself
# syntax of xpath = //tagname[@attribute = 'xxxx']
# every function should accomplish only one single task
class OrangeHrm:

    # what is self keyword , what does __init__
    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com"
        self.driver = webdriver.Chrome()
        self.username = "Admin"
        self.password = "admin123"
        self.username_locator_name_tag = "username"
        self.password_locator_name_tag = "password"

    def browse(self):
        """
        1. browse orange hrm
        2. maximize the window
        :return: None
        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    def input_credentials(self):
        """
        Provide the credential - username and the password
        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.username_locator_name_tag)
        username_webelement.send_keys(self.username)

        password_webelement = self.driver.find_element(By.NAME, self.password_locator_name_tag)
        password_webelement.send_keys(self.password)

        sleep(2)
        #  login button on orange hrm
        login_path_xpath = '//button[@type="submit"]'
        login_button_webelement = self.driver.find_element(By.XPATH, login_path_xpath)
        login_button_webelement.click()

    def cookies_fom_orange_hrm(self):
        """
        retrns the cookies
        :return: this function will return a string saying hello world
        """
        return self.driver.get_cookies()


obj = OrangeHrm()
obj.browse()
sleep(1)
beforelogin_cookies = obj.cookies_fom_orange_hrm()
obj.input_credentials()
after_login_cookies = obj.cookies_fom_orange_hrm()
if beforelogin_cookies == after_login_cookies:
    print("login failed ")
else:
    print("login passed")
print(obj)

abc = [{'domain': 'opensource-demo.orangehrmlive.com',
        'httpOnly': True, 'name': 'orangehrm', 'path': '/web', 'sameSite': 'Strict',
        'secure': True, 'value': '696887e52c18311d5de391528aff7e9c'}]
