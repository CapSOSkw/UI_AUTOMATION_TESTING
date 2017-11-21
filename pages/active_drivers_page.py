from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import Page
from locators.locators import *
import time
import random
from selenium.webdriver.support.ui import Select
import config

class ActiveDriverPage(Page):
    def __init__(self, context):
        Page.__init__(self,context)

    def wait_time(self):
        time.sleep(5)

    def click_active_driver_tab(self):
        try:
            self.find_element(*NavigationPageLocators.ACTIVE_TAB).click()
        except:
            pass

    def verify_active_driver_page_elements(self):
        self.find_element(*ActiveDriverLocators.SEARCHING_BOX)
        self.find_element(*ActiveDriverLocators.TABLE_ID)
        self.find_element(*ActiveDriverLocators.TABLE_NAME)
        self.find_element(*ActiveDriverLocators.TABLE_USERNAME)
        self.find_element(*ActiveDriverLocators.TABLE_EMAIL)
        self.find_element(*ActiveDriverLocators.TABLE_CREATED_DATE)

    def click_active_id(self):
        self.find_element(*ActiveDriverLocators.TABLE_ID).click()

    def click_active_fleet_nnumber(self):
        self.find_element(*ActiveDriverLocators.TABLE_FLEET_NUMBER).click()

    def click_active_status(self):
        self.find_element(*ActiveDriverLocators.TABLE_STATUS).click()

    def click_active_name(self):
        self.find_element(*ActiveDriverLocators.TABLE_NAME).click()

    def click_active_username(self):
        self.find_element(*ActiveDriverLocators.TABLE_USERNAME).click()

    def click_active_email(self):
        self.find_element(*ActiveDriverLocators.TABLE_EMAIL).click()

    def click_active_phone(self):
        self.find_element(*ActiveDriverLocators.TABLE_PHONE).click()

    def click_active_vehicle_id(self):
        self.find_element(*ActiveDriverLocators.TABLE_VEHICLE_ID).click()

    def click_active_base(self):
        self.find_element(*ActiveDriverLocators.TABLE_BASE).click()

    def click_active_duty_status(self):
        self.find_element(*ActiveDriverLocators.TABLE_DUTY_STATUS).click()

    def click_active_created_date(self):
        self.find_element(*ActiveDriverLocators.TABLE_CREATED_DATE).click()

    def click_action_edit_1st_user(self):
        self.find_element(*ActiveDriverLocators.ACTION_EDIT_1ST_USER).click()

    def clear_active_information(self):
        self.find_element(*ActiveDriverLocators.EDIT_FIRST_NAME).clear()
        self.find_element(*ActiveDriverLocators.EDIT_LAST_NAME).clear()
        self.find_element(*ActiveDriverLocators.EDIT_USERNAME).clear()
        self.find_element(*ActiveDriverLocators.EDIT_EMAIL).clear()
        self.find_element(*ActiveDriverLocators.EDIT_PHONE_NUMBER).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DATE_OF_BIRTH).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRIVING_EXP).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_NUMBER).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_CLASS).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_START_DATE).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_EXP_DATE).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_TLC_FHV_NUMBER).clear()
        self.find_element(*ActiveDriverLocators.EDIT_TLC_FHV_START_DATE).clear()
        self.find_element(*ActiveDriverLocators.EDIT_TLC_FHV_EXP_DATE).clear()
        self.find_element(*ActiveDriverLocators.EDIT_BACKGROUND_CHECK_START_DATE).clear()
        self.find_element(*ActiveDriverLocators.EDIT_BACKGROUND_CHECK_EXP_DATE).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRIVING_RECORD_START_DATE).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRIVING_RECORD_EXP_DATE).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRUG_SCREEN_START_DATE).clear()
        self.find_element(*ActiveDriverLocators.EDIT_DRUG_SCREEN_EXP_DATE).clear()

    def enter_active_firstname(self,first_name):
        self.find_element(*ActiveDriverLocators.EDIT_FIRST_NAME).send_keys(first_name)

    def enter_active_lastname(self,last_name):
        self.find_element(*ActiveDriverLocators.EDIT_LAST_NAME).send_keys(last_name)

    def enter_active_username(self,username):
        config.test_data_kw['ACTIVE_PAGE'][0]['USERNAME'] = username
        self.find_element(*ActiveDriverLocators.EDIT_USERNAME).send_keys(username)

    def enter_active_email(self, email):
        self.find_element(*ActiveDriverLocators.EDIT_EMAIL).send_keys(email+'@operr.com')

    def enter_active_phone_number(self, phone):
        self.find_element(*ActiveDriverLocators.EDIT_PHONE_NUMBER).send_keys(phone)

    def enter_active_birthday(self, date):
        self.find_element(*ActiveDriverLocators.EDIT_DATE_OF_BIRTH).send_keys(date)

    def enter_active_gender(self):
        try:
            select = Select(self.find_element(*ActiveDriverLocators.EDIT_GENDER))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_active_country(self):
        try:
            select = Select(self.find_element(*ActiveDriverLocators.EDIT_COUNTRY_OF_ORIGIN))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass


    def enter_active_driving_exp(self, year):
        self.find_element(*ActiveDriverLocators.EDIT_DRIVING_EXP).send_keys(year)


    def enter_active_driver_type(self):
        try:
            select = Select(self.find_element(*ActiveDriverLocators.EDIT_DRIVER_TYPE))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass


    def enter_affiliated_company(self):
        try:
            select = Select(self.find_element(*ActiveDriverLocators.EDIT_AFFILI_COMPANY_NAME))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_affiliated_base(self):
        try:
            select = Select(self.find_element(*ActiveDriverLocators.EDIT_AFFILI_BASE_NAME))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass


    def enter_active_driver_license_number(self, number):
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_NUMBER).send_keys(number)

    def enter_active_driver_license_class(self, license_class):
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_CLASS).send_keys(license_class)

    def enter_active_driver_license_state(self):
        try:
            select = Select(self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_STATE))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass


    def enter_active_driver_license_start_date(self, start_date):
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_START_DATE).send_keys(start_date)

    def enter_active_driver_license_exp_date(self, exp_date):
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_EXP_DATE).send_keys(exp_date)

    def enter_TLC_FHV_number(self, number):
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_TLC_FHV_NUMBER).send_keys(number)

    def enter_TLC_FHV_start_date(self,start_date):
        self.find_element(*ActiveDriverLocators.EDIT_TLC_FHV_START_DATE).send_keys(start_date)

    def enter_TLC_FHV_exp_date(self, exp_date):
        self.find_element(*ActiveDriverLocators.EDIT_TLC_FHV_EXP_DATE).send_keys(exp_date)

    def enter_background_check_start_date(self, start_date):
        self.find_element(*ActiveDriverLocators.EDIT_BACKGROUND_CHECK_START_DATE).send_keys(start_date)

    def enter_background_check_exp_date(self,exp_date):
        self.find_element(*ActiveDriverLocators.EDIT_BACKGROUND_CHECK_EXP_DATE).send_keys(exp_date)

    def enter_driving_record_start_date(self, start_date):
        self.find_element(*ActiveDriverLocators.EDIT_DRIVING_RECORD_START_DATE).send_keys(start_date)

    def enter_driving_record_exp_date(self, exp_date):
        self.find_element(*ActiveDriverLocators.EDIT_DRIVING_RECORD_EXP_DATE).send_keys(exp_date)

    def enter_drug_screen_start_date(self,start_date):
        self.find_element(*ActiveDriverLocators.EDIT_DRUG_SCREEN_START_DATE).send_keys(start_date)

    def enter_drug_screen_exp_date(self,exp_date):
        self.find_element(*ActiveDriverLocators.EDIT_DRUG_SCREEN_EXP_DATE).send_keys(exp_date)

    def enter_vehicle_info(self):
        try:
            select = Select(self.find_element(*ActiveDriverLocators.EDIT_VEHICLE_INFO_DROPDOWN))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def click_cross_county_both(self):
        self.find_element(*ActiveDriverLocators.EDIT_CROSS_COUNTY_BOTH_BTN).click()


    def click_edit_submit_btn(self):
        self.find_element(*ActiveDriverLocators.EDIT_SUBMIT_BTN).click()

    def click_add_a_new_driver(self):
        self.find_element(*ActiveDriverLocators.ADD_NEW_DRIVER_BTN).click()

    def verify_information_exists(self):
        self.find_element(*ActiveDriverLocators.EDIT_FIRST_NAME)
        self.find_element(*ActiveDriverLocators.EDIT_LAST_NAME)
        self.find_element(*ActiveDriverLocators.EDIT_EMAIL)
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_LICENSE_NUMBER)
        self.find_element(*ActiveDriverLocators.EDIT_DRUG_SCREEN_START_DATE)
        self.find_element(*ActiveDriverLocators.EDIT_CROSS_COUNTY_BOTH_BTN)


    def verify_new_username_exist(self):
        s = config.test_data_kw['ACTIVE_PAGE'][0]['USERNAME']
        NEW_USERNAME = (By.XPATH, "//*[contains(text()," + "'%s')]" %s)
        self.find_element(*NEW_USERNAME)

    def enter_dsp_percent(self,value):
        self.find_element(*ActiveDriverLocators.EDIT_DSP_PERCENT).send_keys(value)


    def enter_base_percent(self,value):
        self.find_element(*ActiveDriverLocators.EDIT_BASE_PERCENT).send_keys(value)

    def enter_driver_percent(self,value):
        self.find_element(*ActiveDriverLocators.EDIT_DRIVER_PERCENT).send_keys(value)

    def enter_reserve_percent(self,value):
        self.find_element(*ActiveDriverLocators.EDIT_RESERVE_PERCENT).send_keys(value)

    def click_base_approved_active(self):
        self.find_element(*ActiveDriverLocators.BASE_APPROVED_ACTIVE_BTN).click()

    def enter_password(self,password):
        self.find_element(*ActiveDriverLocators.EDIT_PASSWORD).send_keys(password)