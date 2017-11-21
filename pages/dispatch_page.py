from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import Page
from locators.locators import *
import time
import random, string
from selenium.webdriver.support.ui import Select
import config

class DispatchPage(Page):
    def __init__(self, context):
        Page.__init__(self, context)

    def wait_time(self):
        time.sleep(5)


    def click_dispatch_navigation_tab(self):
        self.find_element(*NavigationPageLocators.DISPATCHING_TAB).click()

    def verify_dispatch_elements_exist(self):
        self.find_element(*DispatchingPageLocators.SHOW_ALL_BOOKING)
        self.find_element(*DispatchingPageLocators.ADD_A_NEW_BOOKING)
        self.find_element(*DispatchingPageLocators.TABLE_TRIP_ID)
        self.find_element(*DispatchingPageLocators.TABLE_AGEBCY_NAME)
        self.find_element(*DispatchingPageLocators.TABLE_DRIVER)

    def click_table_trip_id(self):
        self.find_element(*DispatchingPageLocators.TABLE_TRIP_ID).click()

    def click_table_ts(self):
        self.find_element(*DispatchingPageLocators.TABLE_TS).click()

    def click_table_rs(self):
        self.find_element(*DispatchingPageLocators.TABLE_RS).click()

    def click_agency_name(self):
        self.find_element(*DispatchingPageLocators.TABLE_AGEBCY_NAME).click()

    def click_insurance_id(self):
        self.find_element(*DispatchingPageLocators.TABLE_INSURANCE_ID).click()

    def click_pickup_date(self):
        self.find_element(*DispatchingPageLocators.TABLE_PICKUP_DATE).click()

    def click_passenger_name(self):
        self.find_element(*DispatchingPageLocators.TABLE_PASSENGER_NAME).click()

    def click_passenger_phone(self):
        self.find_element(*DispatchingPageLocators.TABLE_PASSENGER_PHONE).click()

    def click_passenger_email(self):
        self.find_element(*DispatchingPageLocators.TABLE_PASSENGER_EMAIL).click()

    def click_pickup_location(self):
        self.find_element(*DispatchingPageLocators.TABLE_PICKUP_LOCATION).click()

    def click_destination_location(self):
        self.find_element(*DispatchingPageLocators.TABLE_DESTINATION_LOCATION).click()

    def click_table_driver(self):
        self.find_element(*DispatchingPageLocators.TABLE_DRIVER).click()

    def click_add_a_new_booking(self):
        self.find_element(*DispatchingPageLocators.ADD_A_NEW_BOOKING).click()

    def verify_dispatch_edit_elements_exist(self):
        self.find_element(*DispatchingPageLocators.EDIT_COMPANY_NAME)
        self.find_element(*DispatchingPageLocators.EDIT_BASE_NAME)

    def enter_company_name(self):
        try:
            select = Select(self.find_element(*DispatchingPageLocators.EDIT_COMPANY_NAME))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_base_name(self):
        try:
            select = Select(self.find_element(*DispatchingPageLocators.EDIT_BASE_NAME))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_first_name(self, name):
        el = self.find_element(*DispatchingPageLocators.EDIT_FIRST_NAME_DROPDOWN)
        # self.browser.implicitly_wait(10)
        el.click()
        time.sleep(5)
        el2 = self.find_element(*DispatchingPageLocators.EDIT_FIRST_NAME_BOX)
        el2.send_keys(name)

    def enter_last_name(self, name):
        self.find_element(*DispatchingPageLocators.EDIT_LAST_NAME).send_keys(name)

    def enter_phone_number(self,phone):
        self.find_element(*DispatchingPageLocators.EDIT_PHONE_NUMBER).send_keys(phone)


    def click_one_way(self):
        self.find_element(*DispatchingPageLocators.EDIT_ONE_WAY_BTN).click()

    def click_round_trip(self):
        self.find_element(*DispatchingPageLocators.EDIT_ROUND_TRIP_BTN).click()

    def click_trip_type(self):
        try:
            select = Select(self.find_element(*DispatchingPageLocators.EDIT_TRIP_TYPE))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_trip_info(self):
        self.find_element(*DispatchingPageLocators.EDIT_DISPATCH_IMM).click()

        try:
            self.find_element(*DispatchingPageLocators.EDIT_PICKUP_TIME).clear()
            self.find_element(*DispatchingPageLocators.EDIT_PICKUP_TIME).send_keys('01/10/2017 10:00')

        except:
            pass

        try:
            self.find_element(*DispatchingPageLocators.EDIT_RETURN_TIME).clear()
            self.find_element(*DispatchingPageLocators.EDIT_RETURN_TIME).send_keys('10/10/2017 10:00')

        except:
            pass

        try:
            self.find_element(*DispatchingPageLocators.EDIT_PICKUP_LOCATION).send_keys('10086 Central St.')

        except:
            pass

        try:
            self.find_element(*DispatchingPageLocators.EDIT_DESTINATION_LOCATION).send_keys('20086 HL AVE')

        except:
            pass


        try:
            select = Select(self.find_element(*DispatchingPageLocators.EDIT_VEHICLE_TYPE))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass


        try:
            self.find_element(*DispatchingPageLocators.EDIT_INSURANCE_ID).send_keys('666666')

        except:
            pass

        try:
            self.find_element(*DispatchingPageLocators.EDIT_INSURANCE_ID2).send_keys('888888')

        except:
            pass

        try:
            select = Select(self.find_element(*DispatchingPageLocators.EDIT_AGENCY_NAME))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

        try:
            select = Select(self.find_element(*DispatchingPageLocators.EDIT_FARE_TYPE))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass


        try:
            self.find_element(*DispatchingPageLocators.EDIT_ESTIMATED_FARE).send_keys('100')

        except:
            pass

    def click_driver_auto_assign(self):
        self.find_element(*DispatchingPageLocators.EDIT_DRIVER_AUTO).click()

    def click_dispatch_submit(self):
        self.find_element(*DispatchingPageLocators.DISPATCH_SUBMIT_BTN).click()