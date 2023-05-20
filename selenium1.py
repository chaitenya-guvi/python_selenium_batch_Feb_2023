from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()  # instantiating the class
url = "https://www.makemytrip.com/"   # is to try and open 5 different websites
driver.get(url)  # open a webpage
driver.maximize_window()
assert "MakeMyTrip" in driver.title
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
sleep(5)
driver.close()