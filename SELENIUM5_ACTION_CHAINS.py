from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class ActionChainsTrial:
    url = 'https://opensource-demo.orangehrmlive.com'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    username = 'Admin'
    password = 'admin123'
    # Locators for Login
    username_locator = 'username'
    password_locator = 'password'
    submitButton_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    # Locators for Logout
    dropDown_locator = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p'
    logoutButton_locator = 'Logout'

    # Login into the application using normal Python Selenium
    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitButton_locator).click()

    # Logout from the application using ActionChains and normal Python Selenium
    def logout(self):
        sleep(5)
        dropDown_locator = self.driver.find_element(by=By.XPATH, value=self.dropDown_locator)
        # Create the ActionChains Object which will take webdriver as an argument

        action = ActionChains(self.driver)
        # Tell the ActionChains to Click on the HTML Element
        # perform() should be used so that ActionChain can be done successfully

        action.click(on_element=dropDown_locator).perform()
        sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=self.logoutButton_locator).click()


ActionChainsTrial().login()

ActionChainsTrial().logout()
