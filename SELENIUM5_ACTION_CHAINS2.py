from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class ActionChainsDrag():
    url = 'https://qavbox.github.io/demo/dragndrop/'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Create the ActionChains Object which will take webdriver as an argument    
    action = ActionChains(driver)
    source_1 = 'draggable'
    target_1 = 'droppable'

    # Browsing Method
    def Browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # ActionChains Drag and Drop
    def Drag_Drop(self):
        sleep(5)
        source_1 = self.driver.find_element(by=By.ID, value=self.source_1)
        target_1 = self.driver.find_element(by=By.ID, value=self.target_1)
        self.action.drag_and_drop(source_1, target_1).perform()

    # ActionChains Drag and Drop Offset
    def Drag_Drop_Offset(self):
        sleep(5)
        source_1 = self.driver.find_element(by=By.ID, value=self.source_1)
        target_1 = self.driver.find_element(by=By.ID, value=self.target_1)
        self.action.drag_and_drop_by_offset(source_1, -200, 100).perform()

    def move_slider(self):
        sleep(2)
        xpath_of_slider = '//input[@type="range"]'
        webelement_slider = self.driver.find_element(By.XPATH, xpath_of_slider)
        self.action.drag_and_drop_by_offset(webelement_slider, 50, 0).perform()
        sleep(4)
        self.action.drag_and_drop_by_offset(webelement_slider, -20, 0).perform()
        sleep(4)
        self.action.key_up()


ActionChainsDrag().Browsing()
# ActionChainsDrag().Drag_Drop()
# ActionChainsDrag().Drag_Drop_Offset()
ActionChainsDrag().move_slider()
