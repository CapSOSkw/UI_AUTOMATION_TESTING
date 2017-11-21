from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.locators import *
import unittest
import time

class Page(unittest.TestCase):
    def __init__(self, context):
        self.browser = context.browser

    def find_element(self, *locator):
        self.browser.implicitly_wait(10)
        time.sleep(1)
        return self.browser.find_element(*locator)

    def open(self,url):
        self.browser.get(url)

        



