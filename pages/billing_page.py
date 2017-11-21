
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains  import ActionChains
from .base import Page
from locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait
# from bs4 import BeautifulSoup
import time
import random
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta

import config
# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes
class BillingPage(Page):

    def __init__(self, context):
        Page.__init__(
            self,
            context)

    def visit_billing_page(self):
        self.find_element(*NavigationPageLocators.BILLING_TAB).click()
    def verify_companyinfo_dropdown_exists(self):
        self.find_element(*BillingPageLocators.COMPANYINFO_DROPDOWN)
    def verify_agencyname_dropdown_exsits(self):
        self.find_element(*BillingPageLocators.AGENCYNAME_DROPDOWN)
    def verify_calendar_exists(self):
        self.find_element(*BillingPageLocators.CALENDAR_DROPDOWN)
    def verify_submit_button_exists(self):
        self.find_element(*BillingPageLocators.SUBMIT_BUTTON)
    def click_the_reportrange_textbox(self):
        self.find_element(*BillingPageLocators.CALENDAR_DROPDOWN).click()
        self.find_element(*BillingPageLocators.TODAY_BUTTON)
    def verify_today_button(self):
        self.find_element(*BillingPageLocators.TODAY_BUTTON).click()
        dateValue = self.find_element(*BillingPageLocators.CALENDAR_DROPDOWN).text
        assert (time.strftime("%B %d")) in dateValue
    def verify_yesterday_button(self):
        self.find_element(*BillingPageLocators.YESTERDAY_BUTTON).click()
        dateValue = self.find_element(*BillingPageLocators.CALENDAR_DROPDOWN).text
        yesterday = datetime.now() - timedelta(days=1)
        assert (yesterday.strftime("%B %d")) in dateValue
    def verify_last7days_button(self):
        self.find_element(*BillingPageLocators.LAST7DAYS_BUTTON).click()
        dateValue = self.find_element(*BillingPageLocators.CALENDAR_DROPDOWN).text
        yesterday = datetime.now() - timedelta(days=6)
        assert (yesterday.strftime("%B %d")) in dateValue
        assert (time.strftime("%B %d")) in dateValue

    def verify_last30days_button(self):
        self.find_element(*BillingPageLocators.LAST30DAYS_BUTTON).click()
        dateValue = self.find_element(*BillingPageLocators.CALENDAR_DROPDOWN).text
        yesterday = datetime.now() - timedelta(days=29)
        assert (yesterday.strftime("%B %d")) in dateValue
        assert (time.strftime("%B %d")) in dateValue
    def verify_thismonth_button(self):
        self.find_element(*BillingPageLocators.THISMONTH_BUTTON).click()
        dateValue = self.find_element(*BillingPageLocators.CALENDAR_DROPDOWN).text
        d=date.today()
        begin_date = str(d.strftime("%B 1, %Y"))
        end_date = date(d.year, d.month, 1) - relativedelta(days=1) + relativedelta(months=1)
        assert begin_date,end_date in dateValue
    def verify_lastmonth_button(self):
        self.find_element(*BillingPageLocators.LASTMONTH_BUTTON).click()
        dateValue = self.find_element(*BillingPageLocators.CALENDAR_DROPDOWN).text
        d = date.today()
        begin_date = date(d.year, d.month, 1)
        end_date = date(d.year, d.month, 1) - relativedelta(days=1) - relativedelta(months=1)
        assert begin_date, end_date in dateValue
    def select_companyinfo_dropdown(self):
        select = Select(self.find_element(*BillingPageLocators.COMPANYINFO_DROPDOWN))
        options = [o.text for o in select.options]
        option = random.choice(options[1:])
        select.select_by_visible_text(option)
    def select_baseinfo_dropdown(self):
        select = Select(self.find_element(*BillingPageLocators.BASEINFO_DROPDOWN))
        options = [o.text for o in select.options]
        option = random.choice(options[1:])
        select.select_by_visible_text(option)
    def select_agencyname_dropdown(self):
        select = Select(self.find_element(*BillingPageLocators.AGENCYNAME_DROPDOWN))
        options = [o.text for o in select.options]
        option = random.choice(options)
        select.select_by_visible_text(option)
    def select_driverinfo_dropdown(self):
        select = Select(self.find_element(*BillingPageLocators.DRIVER_INFO))
        options = [o.text for o in select.options]
        option = random.choice(options)
        select.select_by_visible_text(option)
    def submit_search_critira(self):
        self.find_element(*BillingPageLocators.SUBMIT_BUTTON).click()
        self.find_element(*BillingPageLocators.RESULT_BAR)
    def cancel_calendar_search(self):
        self.find_element(*BillingPageLocators.CANCEL_SEARCH).click()









