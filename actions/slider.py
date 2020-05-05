from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class Slider():
    def test(self):
        baseURL = 'https://jqueryui.com/slider/'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        actions = ActionChains(driver)
        driver.switch_to.frame(0)
        element = driver.find_element(By.XPATH,'//div[@id="slider"]//span')
        time.sleep(3)
        actions.drag_and_drop_by_offset(element,550,0).perform()
        time.sleep(3)


ff = Slider()
ff.test()