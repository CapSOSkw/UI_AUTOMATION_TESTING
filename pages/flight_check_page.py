from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains  import ActionChains
from .base import Page
from locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import Page
import time
import config


class FlightCheckPage(Page):
    def __init__(self, context):
        Page.__init__(self,context)

    def wait_time(self):
        time.sleep(5)

    def click_flight_check_navigation_tab(self):
        self.find_element(*NavigationPageLocators.FLIGHT_CHECK).click()

    def verify_flight_elements_exist(self):
        self.find_element(*FlightCheckPageLocators.DEPARTING_DATE)
        self.find_element(*FlightCheckPageLocators.AIRLINE)
        self.find_element(*FlightCheckPageLocators.FLIGHT_NUMBER)

    def enter_date_before_or_after(self, value):
        today = date.today()
        if value >= 0:
            d = date(today.year, today.month, today.day) + relativedelta(days=value)
            year,month,day = d.year, d.month, d.day
            self.find_element(*FlightCheckPageLocators.DEPARTING_DATE).send_keys(str(month) + '/' + str(day) + '/' + str(year))
        elif value<0:
            d = date(today.year, today.month, today.day) - relativedelta(days=value)
            year, month, day = d.year, d.month, d.day
            self.find_element(*FlightCheckPageLocators.DEPARTING_DATE).send_keys(str(month) + '/' + str(day) + '/' + str(year))


    def enter_airline(self, airline):
        self.find_element(*FlightCheckPageLocators.AIRLINE).send_keys(airline)

    def enter_flight_number(self, number):
        config.test_data_kw['FLIGHT_PAGE'][0]['FLIGHT_NUMBER'] = number
        self.find_element(*FlightCheckPageLocators.FLIGHT_NUMBER).send_keys(number)

    def click_search_button(self):
        self.find_element(*FlightCheckPageLocators.SEARCH_BTN).click()

    def verify_checked_flight_number_exists(self):
        s = config.test_data_kw['FLIGHT_PAGE'][0]['FLIGHT_NUMBER']
        NEW_NUMBER = (By.XPATH, "//*[contains(text()," + "'%s')]" % s)
        self.find_element(*NEW_NUMBER)