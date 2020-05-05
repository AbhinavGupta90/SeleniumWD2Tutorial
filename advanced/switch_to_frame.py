from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame():
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,1000);")
        # driver.switch_to.frame('courses-iframe')
        # driver.switch_to.frame('iframe-name')
        driver.switch_to.frame(0)
        driver.find_element_by_id('search-courses').send_keys('python')
        time.sleep(5)
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(5)
        driver.find_element_by_id('name').send_keys('Success')

ff = SwitchToFrame()
ff.test()
