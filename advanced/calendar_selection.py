from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class CalendarSelection():
    def test1(self):
        baseURL = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id('tab-flight-tab-hp').click()
        # Find departing field
        departingField = driver.find_element_by_id('flight-departing-hp-flight')
        # Click departing field
        departingField.click()
        # Find the date to be selected
        dateToSelect = driver.find_element(By.XPATH, '//div[@class="datepicker-cal-month"]//tr[5]//td[5]')
        # Click the date
        dateToSelect.click()

        time.sleep(3)
        driver.quit()


ff = CalendarSelection()
ff.test1()
