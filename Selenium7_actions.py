from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class Practice:

    def __init__(self):
        self.driver = webdriver.Chrome()
        # service=Service(ChromeDriverManager().install()))
        self.url = "https://www.letskodeit.com/practice"
        self.top_xpath = '//a[@href="#top"]'

    def browse(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        #         Click on the top button
        self.driver.execute_script("window.scrollBy(0,660);")


            #      for initializing Action class we need to pass the driver object
        actions_obj = ActionChains(self.driver)

        mousehover_id = 'mousehover'
        mousehover_webelement = self.driver.find_element(By.ID, mousehover_id)
        # no Action chain is successfull without perform function
        actions_obj.move_to_element(mousehover_webelement).perform()
        time.sleep(5)

        top_webelement = self.driver.find_element(By.XPATH, self.top_xpath)
        top_webelement.click()
        time.sleep(5)



obj = Practice()
obj.browse()
