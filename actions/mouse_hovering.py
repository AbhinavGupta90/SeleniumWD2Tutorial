from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class MouseHovering():
    def test(self):
        baseURL = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollTo(0,900);")
        mouseHoverButton = driver.find_element_by_id('mousehover')
        topButton = driver.find_element(By.XPATH,'//div[@class="mouse-hover-content"]//a[text()="Top"]')

        try:
            actions = ActionChains(driver)
            time.sleep(5)
            actions.move_to_element(mouseHoverButton).perform()
            print('Mouse hovered on element')
            actions.move_to_element(topButton).click().perform()
            print('Top link clicked')
            time.sleep(5)
        except:
            print('Mouse hovering failed on element')


ff = MouseHovering()
ff.test()
