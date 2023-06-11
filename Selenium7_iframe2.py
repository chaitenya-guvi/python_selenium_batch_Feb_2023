from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class FrameSelect():

    def test1(self):
        """

        # baseUrl = "https://letskodeit.teachable.com/pages/practice"
        # baseUrl = "https://the-internet.herokuapp.com/iframe"
        # baseUrl = "https://the-internet.herokuapp.com/iframe"

        1. navigate to base page - done
        2. navigate to the iframe - done
        3. navigate with the elements inside the iframe - done

        :return:
        """

        baseUrl = "https://jqueryui.com/selectmenu/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        # switching to iframe inside the page
        xpath_of_iframe = "//iframe"
        iframe_1 = driver.find_element(By.XPATH,xpath_of_iframe)
        #syntax for switching
        driver.switch_to.frame(iframe_1)
        time.sleep(6)
        # Select class example
        xpath_ofselect_speed = "speed"
        sel_element = driver.find_element(By.ID,xpath_ofselect_speed)
        sel = Select(sel_element)
        sel_element.click()
        sel.select_by_visible_text("Slower")

        time.sleep(10)
        driver.quit()

    def test_2(self):
        baseUrl = "https://the-internet.herokuapp.com/iframe"

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(5)
        driver.switch_to.frame(driver.find_element(By.XPATH , "//iframe"))

        text_editor = driver.find_element(By.ID,"tinymce")

        text_editor_paragraph = text_editor.find_element(By.XPATH,"//p")
        time.sleep(5)
        text_editor.clear()
        time.sleep(5)
        text_editor.send_keys("hello_world")
        time.sleep(10)
        driver.quit()




ff = FrameSelect()
# ff.test1()
ff.switch_to_alert()
# ff.test_2()
