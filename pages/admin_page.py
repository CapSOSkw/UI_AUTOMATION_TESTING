from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import Page
from locators.locators import *
import time
import random
from selenium.webdriver.support.ui import Select
import config

class AdminPage(Page):
    def __init__(self, context):
        Page.__init__(self, context)

    def wait_time(self):
        time.sleep(5)

    def verify_admin_page_elements(self):
        self.find_element(*AdminPageLocators.SHOW_ALL_ADMIN_BTN)
        self.find_element(*AdminPageLocators.ADD_NEW_ADMIN_BTN)
        self.find_element(*AdminPageLocators.ADMIN_MENU_BTN)
        self.find_element(*AdminPageLocators.SEARCHING_TYPE_DROPDOWN)
        self.find_element(*AdminPageLocators.SEARCHING_BOX)
        self.find_element(*AdminPageLocators.SEARCHING_BTN)
        self.find_element(*AdminPageLocators.TABLE_STATUS)
        self.find_element(*AdminPageLocators.TABLE_USERNAME)
        self.find_element(*AdminPageLocators.TABLE_EMAIL)
        self.find_element(*AdminPageLocators.TABLE_PHONE)
        self.find_element(*AdminPageLocators.TABLE_2ND_PHONE)
        self.find_element(*AdminPageLocators.TABLE_ADMIN_LVL)
        self.find_element(*AdminPageLocators.TABLE_COMPANY)
        self.find_element(*AdminPageLocators.TABLE_BASE)
        self.find_element(*AdminPageLocators.TABLE_ADDRESS)
        self.find_element(*AdminPageLocators.TABLE_NAME)

    def click_admin_tab(self):
        try:
            admin_tab = self.find_element(*NavigationPageLocators.ADMIN_TAB)
            admin_tab.click()
        except:
            pass

    def click_table_status(self):
        self.find_element(*AdminPageLocators.TABLE_STATUS).click()

    def click_table_username(self):
        try:
            self.find_element(*AdminPageLocators.TABLE_USERNAME).click()
        except:
            pass

    def click_table_email(self):
        self.find_element(*AdminPageLocators.TABLE_EMAIL).click()

    def click_table_phone(self):
        self.find_element(*AdminPageLocators.TABLE_PHONE).click()

    def click_table_2ndphone(self):
        self.find_element(*AdminPageLocators.TABLE_2ND_PHONE).click()

    def click_table_admin_lvl(self):
        self.find_element(*AdminPageLocators.TABLE_ADMIN_LVL).click()

    def click_table_company(self):
        self.find_element(*AdminPageLocators.TABLE_COMPANY).click()

    def click_table_base(self):
        self.find_element(*AdminPageLocators.TABLE_BASE).click()

    def click_table_address(self):
        self.find_element(*AdminPageLocators.TABLE_ADDRESS).click()

    def click_table_name(self):
        self.find_element(*AdminPageLocators.TABLE_NAME).click()

    def enter_text_in_search_box(self,searching_text):
        # searching_text = self.find_element(*AdminPageLocators.SEARCHING_TEXT).text.lower()
        self.find_element(*AdminPageLocators.SEARCHING_BOX).send_keys(searching_text)

    def click_searching_btn(self):
        self.find_element(*AdminPageLocators.SEARCHING_BTN).click()

    def click_add_new_admin_btn(self):
        self.find_element(*AdminPageLocators.ADD_NEW_ADMIN_BTN).click()

    def enter_firstname(self,first_name):
        self.find_element(*AdminPageLocators.FIRST_NAME_BOX).send_keys(first_name)

    def enter_lastname(self,last_name):
        self.find_element(*AdminPageLocators.LAST_NAME_BOX).send_keys(last_name)

    def enter_username(self,username):
        config.test_data_kw['ADMIN_PAGE'][0]['USERNAME'] = username
        self.find_element(*AdminPageLocators.USERNAME_BOX).send_keys(username)

    def enter_email_address(self,email):
        self.find_element(*AdminPageLocators.EMAIL_BOX).send_keys(email+'@operr.com')

    def enter_password(self,password):
        self.find_element(*AdminPageLocators.PASSWORD_BOX).send_keys(password)

    def enter_add_phone(self,phone):
        self.find_element(*AdminPageLocators.PHONE_BOX_ADD).send_keys(phone)

    def enter_edit_phone(self,phone):
        self.find_element(*AdminPageLocators.PHONE_BOX_EDIT).send_keys(phone)

    def choose_permission_lvl_EDIT(self):
        try:
            select = Select(self.find_element(*AdminPageLocators.PERMISSION_LVL_DROPDOWN_EDIT))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def choose_permission_lvl_ADD(self):
        try:
            select = Select(self.find_element(*AdminPageLocators.PERMISSION_LVL_DROPDOWN_ADD))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def choose_company_EDIT(self):
        try:
            select = Select(self.find_element(*AdminPageLocators.COMPANY_DROPDOWN_EDIT))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def choose_company_ADD(self):
        try:
            select = Select(self.find_element(*AdminPageLocators.COMPANY_DROPDOWN_ADD))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def choose_base_EDIT(self):
        try:
            select = Select(self.find_element(*AdminPageLocators.BASE_DROPDOWN_EDIT))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def choose_base_ADD(self):
        try:
            select = Select(self.find_element(*AdminPageLocators.BASE_DROPDOWN_ADD))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def click_active(self):
        self.find_element(*AdminPageLocators.STATUS_ACTIVE).click()

    def click_inactive(self):
        self.find_element(*AdminPageLocators.STATUS_INACTIVE).click()

    def click_submit_btn(self):
        self.find_element(*AdminPageLocators.SUBMIT_BTN).click()

    def verify_new_username_exist(self):
        s = config.test_data_kw['ADMIN_PAGE'][0]['USERNAME']
        USERNAME = (By.XPATH, "//*[contains(text()," + "'%s')]" %s)
        self.find_element(*USERNAME)

    def click_action_btn(self):
        self.find_element(*AdminPageLocators.ACTION_BTN_1ST_USER).click()

    def click_status_active(self):
        self.find_element(*AdminPageLocators.STATUS_ACTIVE).click()

    def click_submit_button_edit_page(self):
        self.find_element(*AdminPageLocators.SUBMIT_EDIT_BTN).click()

    def clear_all_information(self):
        self.find_element(*AdminPageLocators.FIRST_NAME_BOX).clear()
        self.find_element(*AdminPageLocators.LAST_NAME_BOX).clear()
        self.find_element(*AdminPageLocators.USERNAME_BOX).clear()
        self.find_element(*AdminPageLocators.EMAIL_BOX).clear()
        self.find_element(*AdminPageLocators.PHONE_BOX_EDIT).clear()

    def verify_edit_admin_elements_exist(self):
        self.find_element(*AdminPageLocators.FIRST_NAME_BOX)
        self.find_element(*AdminPageLocators.LAST_NAME_BOX)
        self.find_element(*AdminPageLocators.USERNAME_BOX)
        self.find_element(*AdminPageLocators.EMAIL_BOX)
        self.find_element(*AdminPageLocators.PHONE_BOX_EDIT)


    def verify_search_result(self):
        admin_search = (By.XPATH, '//*[contains(text(), "Cheng")]')
        self.find_element(*admin_search)

    def clear_search_box(self):
        self.find_element(*AdminPageLocators.SEARCHING_BOX).clear()
        self.find_element(*AdminPageLocators.SEARCHING_BTN).click()