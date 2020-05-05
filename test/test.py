from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Testing():
    def abc(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        #print("Element appeared on the web page")


cl = Testing()
cl.abc()
