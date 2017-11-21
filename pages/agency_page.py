from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import Page
from locators.locators import *
import time
import config
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class AgencyPage(Page):
    def __init__(self, context):
        Page.__init__(
            self,
            context)

    def visit_agency_page(self):
        self.find_element(*NavigationPageLocators.AGENCY_TAB).click()
    def verify_agency_banner(self):
        self.find_element(*AgencyLocators.OPERR_AGENCY_VIEW_ALL_BANNER)
    def verify_show_entries(self):
        self.find_element(*AgencyLocators.SHOW_ENTRIES_DROPDOWN)
    def verify_search_column(self):
        self.find_element(*AgencyLocators.SEARCHING_BTN)
        self.find_element(*AgencyLocators.SEARCHING_COLUMUN)
        self.find_element(*AgencyLocators.SEARCHING_TEXTBOX)
    def verify_active_lable(self):
        self.find_element(*AgencyLocators.ACTIVE_LABLE)
    def verify_agency_tab(self):
        self.find_element(*AgencyLocators.ADD_A_NEW_AGENCY_TAB)
        self.find_element(*AgencyLocators.SHOW_ALL_AGENCIES_TAB)
    def verify_edit_btn(self):
        self.find_element(*AgencyLocators.EDIT_BTN)
    def sort_by_ID(self):
        self.find_element(*AgencyLocators.ID_COLUMN).click()
    def click_edit_btn(self):
        self.find_element(*AgencyLocators.EDIT_BTN).click()
    def click_submit(self):
        self.find_element(*AgencyLocators.SUBMIT).click()
    def edit_agency_info(self,address):
        self.find_element(*AgencyLocators.ADDRESS_TEXTBOX).clear()
        self.find_element(*AgencyLocators.ADDRESS_TEXTBOX).send_keys(address)
    def click_add_an_agency(self):
        self.find_element(*AgencyLocators.ADD_A_NEW_AGENCY_TAB).click()
    def select_agency_type(self):
        select = Select(self.find_element(*AgencyLocators.TYPE_DROPDOWN))
        options = [o.text for o in select.options]
        option = random.choice(options[1:])
        select.select_by_visible_text(option)
    def enter_agency_name(self,name):
        self.find_element(*AgencyLocators.NAME_TEXTBOX).send_keys(name)
    def enter_agency_code(self,code):
        self.find_element(*AgencyLocators.CODE_TEXTBOX).send_keys(code)
    def select_days_in_week(self):
        week_list = [AgencyLocators.MON_POINTER,AgencyLocators.TUE_POINTER,AgencyLocators.WED_POINTER,AgencyLocators.THU_POINTER,AgencyLocators.FRI_POINTER,AgencyLocators.SAT_POINTER,AgencyLocators.SUN_POINTER]
        for i in random.sample(week_list,5):
            self.find_element(*i).click()
    def choose_worktime_start(self,starthour):
        self.find_element(*AgencyLocators.START_HOUR).clear()
        self.find_element(*AgencyLocators.START_HOUR).send_keys(starthour)
    def choose_worktime_end(self,endhour):
        self.find_element(*AgencyLocators.END_HOUR).clear()
        self.find_element(*AgencyLocators.END_HOUR).send_keys(endhour)
    def enter_phone_number(self,phone):
        self.find_element(*AgencyLocators.PHONE_TEXTBOX).send_keys(phone)
    def enter_email(self,email):
        self.find_element(*AgencyLocators.EMAIL_TEXTBOX).send_keys(email)
    def select_state(self):
        select = Select(self.find_element(*AgencyLocators.STATE_DROPDOWN))
        options = [o.text for o in select.options]
        option = random.choice(options[1:])
        select.select_by_visible_text(option)
    def enter_city(self,city):
        self.find_element(*AgencyLocators.CITY_TEXTBOX).send_keys(city)
    def enter_zipcode(self,zipcode):
        self.find_element(*AgencyLocators.ZIP_CODE).send_keys(zipcode)
    def select_active_status(self):
        self.find_element(*AgencyLocators.STATUS_ACTIVE_POINTER).click()


    def choose_search_column(self,agency_name):
        select = Select(self.find_element(*AgencyLocators.SEARCHING_COLUMN))
        options = [o.text for o in select.options]
        select.select_by_visible_text(options[3])
        self.find_element(*AgencyLocators.SEARCHING_TEXTBOX).send_keys(config.test_data["AGENCY_PAGE"][0]["NAME"])
        s = agency_name
        locator = (By.XPATH, '//td[@class="table-cell-center ng-binding"][contains( text( ),"%s")]' % s)
        self.find_element(*AgencyLocators.SEARCHING_BTN).click()
        self.find_element(*locator)















