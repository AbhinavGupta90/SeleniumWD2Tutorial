from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class JavascriptExecution():
    def test(self):
        driver = webdriver.Firefox()
        driver.execute_script('window.location = "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1";')
        driver.implicitly_wait(3)
        element = driver.execute_script("return document.getElementById('user_email');")
        element.send_keys('Test')


ff = JavascriptExecution()
ff.test()
