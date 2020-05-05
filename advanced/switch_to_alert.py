from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToAlert():
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(3)
        driver.find_element_by_id('name').send_keys('Abhinav')
        time.sleep(3)
        driver.find_element_by_id('alertbtn').click()
        time.sleep(3)
        alert1 = driver.switch_to.alert
        time.sleep(3)
        alert1.accept()
        time.sleep(3)
        driver.find_element_by_id('name').send_keys('Abhinav')
        time.sleep(3)
        driver.find_element_by_id('confirmbtn').click()
        time.sleep(3)
        alert2 = driver.switch_to.alert
        time.sleep(3)
        alert2.dismiss()
        time.sleep(3)


ff = SwitchToAlert()
ff.test()