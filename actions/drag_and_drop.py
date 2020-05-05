from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class DragAndDrop():
    def test(self):
        baseURL = 'https://jqueryui.com/droppable/'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.switch_to.frame(0)
        fromElement = driver.find_element_by_id('draggable')
        toElement = driver.find_element_by_id('droppable')
        actions = ActionChains(driver)
        time.sleep(5)
        actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
        #actions.drag_and_drop(fromElement,toElement).perform()
        time.sleep(5)


ff = DragAndDrop()
ff.test()
