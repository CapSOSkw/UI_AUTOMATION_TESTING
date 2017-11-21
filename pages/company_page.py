from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import Page
from locators.locators import *
import time
import random
from selenium.webdriver.support.ui import Select
import config

class CompanyPage(Page):
    def __init__(self, context):
        Page.__init__(self,context)

    def wait_time(self):
        time.sleep(5)

    def click_company_navigation_tab(self):
        try:
            self.find_element(*NavigationPageLocators.COMPANY_TAB).click()
        except:
            pass

    def verify_company_elements_exist(self):
        self.find_element(*CompanyLocators.SEARCHING_BOX)
        self.find_element(*CompanyLocators.TABLE_STATUS)
        self.find_element(*CompanyLocators.TABLE_COMPANY)
        self.find_element(*CompanyLocators.ADD_A_NEW_COMPANY_BTN)

    def click_add_a_new_company_button(self):
        self.find_element(*CompanyLocators.ADD_A_NEW_COMPANY_BTN).click()

    def verify_add_company_elements_exist(self):
        self.find_element(*CompanyLocators.EDIT_COMPANY_NAME)
        self.find_element(*CompanyLocators.WORKTIME_START_HOUR)
        self.find_element(*CompanyLocators.EDIT_PHONE_NUMBER)
        self.find_element(*CompanyLocators.EDIT_ZIPCODE)
        self.find_element(*CompanyLocators.EDIT_STATE)

    def enter_company_name(self, name):
        config.test_data_kw['COMPANY_PAGE'][0]['COMPANY_NAME'] = name
        self.find_element(*CompanyLocators.EDIT_COMPANY_NAME).send_keys(name)

    def enter_days_in_week(self):
        self.find_element(*CompanyLocators.MON).click()
        self.find_element(*CompanyLocators.TUE).click()
        self.find_element(*CompanyLocators.WED).click()
        self.find_element(*CompanyLocators.THU).click()
        self.find_element(*CompanyLocators.FRI).click()

    def enter_start_worktime(self, hour, minute):
        self.find_element(*CompanyLocators.WORKTIME_START_HOUR).clear()
        self.find_element(*CompanyLocators.WORKTIME_START_HOUR).send_keys(hour)
        self.find_element(*CompanyLocators.WORKTIME_START_MIN).clear()
        self.find_element(*CompanyLocators.WORKTIME_START_MIN).send_keys(minute)

    def enter_end_worktime(self, hour, minute):
        self.find_element(*CompanyLocators.WORKTIME_END_HOUR).clear()
        self.find_element(*CompanyLocators.WORKTIME_END_HOUR).send_keys(hour)
        self.find_element(*CompanyLocators.WORKTIME_END_MIN).clear()
        self.find_element(*CompanyLocators.WORKTIME_END_MIN).send_keys(minute)

    def enter_phone_number(self, number):
        self.find_element(*CompanyLocators.EDIT_PHONE_NUMBER).send_keys(number)

    def enter_email(self, email):
        self.find_element(*CompanyLocators.EDIT_EMAIL).send_keys(email+"@operr.com")

    def enter_address(self, address):
        self.find_element(*CompanyLocators.EDIT_ADDRESS).send_keys('123 '+address+' St.')

    def enter_state(self):
        try:
            select = Select(self.find_element(*CompanyLocators.EDIT_STATE))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_city(self, city):
        self.find_element(*CompanyLocators.EDIT_CITY).send_keys(city)

    def enter_zipcode(self,zipcode):
        self.find_element(*CompanyLocators.EDIT_ZIPCODE).send_keys(zipcode)

    def click_active(self):
        self.find_element(*CompanyLocators.ACTIVE_BTN).click()

    def click_inactive(self):
        self.find_element(*CompanyLocators.INACVTIVE_BTN).click()

    def click_submit_btn(self):
        self.find_element(*CompanyLocators.SUBMIT_BTN).click()

    def company_search(self, value):
        self.find_element(*CompanyLocators.SEARCHING_BOX).send_keys(value)

    def click_search_btn(self):
        self.find_element(*CompanyLocators.SEARCHING_BTN).click()

    def verify_new_company_added(self):
        s = config.test_data_kw['COMPANY_PAGE'][0]['COMPANY_NAME']
        NEW_COMPANY = (By.XPATH, "//*[contains(text()," + "'%s')]" %s)
        self.find_element(*NEW_COMPANY)


    def search_company_dropdown(self):
        self.find_element(*CompanyLocators.SEARCHING_DROPDOWN).click()
        self.find_element(*CompanyLocators.SEARCHING_DROPDOWN_COMPANY).click()