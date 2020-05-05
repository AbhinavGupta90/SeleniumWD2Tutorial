from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Screenshots():
    def Test(self):
        baseURL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)

        loginButton = driver.find_element(By.XPATH, '//a[@class="navbar-link fedora-navbar-link"]')
        loginButton.click()
        time.sleep(5)
        driver.find_element_by_id('user_email').send_keys('nsitester1@example.com')
        driver.find_element_by_id('user_password').send_keys('12345')
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        destinationFileName = 'C:\\Users\\ishug\\OneDrive\\Desktop\\image.png'




        try:
            driver.save_screenshot(destinationFileName)
            print('Screenshot saved to directory')
        except NotADirectoryError:
            print('Not a directory issue')

        time.sleep(5)
        driver.quit()


ff = Screenshots()
ff.Test()
