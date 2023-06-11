from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class ABC:

    def switch_to_alert(self):
        baseUrl = "https://the-internet.herokuapp.com/javascript_alerts"

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        time.sleep(5)

        # driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
        driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]').click()
        time.sleep(5)
        alert_element = driver.switch_to.alert

        # alert_element.accept()
        # alert_element.dismiss()
        alert_element.send_keys(" hello_world i am chaitenya ")
        time.sleep(5)
        driver.quit()
