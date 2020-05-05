from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WindowSize():
    def test(self):
        driver = webdriver.Firefox()
        driver.get('https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        height1 = str(height)
        width1 = str(width)
        print("Height of the window is :" + height1)
        print("Width of the window is :" + width1)


ff = WindowSize()
ff.test()


