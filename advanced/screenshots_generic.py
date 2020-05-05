from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScreenshotsGeneric():
    def test1(self):
        baseURL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)
        loginButton = driver.find_element(By.XPATH, '//a[@class="navbar-link fedora-navbar-link"]')
        loginButton.click()
        time.sleep(3)
        emailField = driver.find_element_by_id('user_email')
        emailField.send_keys('nsitester@example.com')
        pwsdField = driver.find_element_by_id('user_password')
        pwsdField.send_keys('123456')
        time.sleep(3)
        submitButton = driver.find_element(By.XPATH, '//input[@type="submit"]')
        submitButton.click()
        time.sleep(3)
        self.test2(driver)

    def test2(self, driver):
        baseLocation = 'C:\\Users\\ishug\\OneDrive\\Desktop\\'
        imageName = str(round(time.time()*1000)) + '.png'
        try:
            imageLocation = baseLocation + imageName
            driver.save_screenshot(imageLocation)
            print('Screenshot saved on the desktop')
        except NotADirectoryError:
            print('There is directory error')

        time.sleep(3)
        driver.quit()


ff = ScreenshotsGeneric()
ff.test1()
