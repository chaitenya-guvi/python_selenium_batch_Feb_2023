from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains


class ActionsChainsDrag:

    def __init__(self):
        self.driver = webdriver.Chrome()
        # service=Service(ChromeDriverManager().install()))
        self.url = "https://the-internet.herokuapp.com/drag_and_drop"
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.id_of_column1 = "column-a"
        self.id_of_column2 = "column-b"

    def drag(self):
        sleep(1)
        action_obj = ActionChains(self.driver)
        source_element = self.driver.find_element(by=By.ID, value=self.id_of_column1)
        target_element = self.driver.find_element(by=By.ID, value=self.id_of_column2)
        # action_obj.drag_and_drop(source=source_element, target=target_element).perform()
        action_obj.click_and_hold(source_element).move_to_element(target_element).release().perform()
        sleep(5)

    def drag_by_offset(self):
        sleep(1)
        action_obj = ActionChains(self.driver)
        source_element_1 = self.driver.find_element(by=By.ID, value=self.id_of_column1)
        target_element_1 = self.driver.find_element(by=By.ID, value=self.id_of_column2)
        action_obj.drag_and_drop_by_offset(source_element_1, 200, 0).perform()
        sleep(5)


obj = ActionsChainsDrag()
# obj.drag()
obj.drag_by_offset()
