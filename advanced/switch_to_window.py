from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow():
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        parentHandle = driver.current_window_handle
        driver.find_element_by_id('openwindow').click()
        time.sleep(5)
        handles = driver.window_handles
        for handle in handles:
            if handle != parentHandle:
                driver.switch_to.window(handle)
                driver.find_element_by_id('search-courses').send_keys('Python')
                time.sleep(5)
                driver.close()
        driver.switch_to.window(parentHandle)
        driver.find_element_by_id('name').send_keys('Success')


ff = SwitchToWindow()
ff.test()