from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():
    def test1(self):
        baseURL = 'https://www.southwest.com/'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)

        Sourcefield1 = driver.find_element_by_id('LandingAirBookingSearchForm_originationAirportCode').clear()
        Sourcefield1.send_keys('New York')
        time.sleep(3)
        airport = driver.find_element(By.XPATH,'')
        airport.click()


ff = AutoComplete()
ff.test1()
