from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScrollingElement():
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Scroll down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(5)
        # Scroll up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(5)
        # Scroll element into view
        element = driver.find_element_by_id('mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,-150)")
        time.sleep(5)
        # Native way to scroll into view
        driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view
        print("Location is : " + str(location))


ff = ScrollingElement()
ff.test()
