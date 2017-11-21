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



class AdminGroupPage(Page):

    def __init__(self, context):
        Page.__init__(
            self,
            context)
    def visit_admin_group_page(self):
        self.find_element(*NavigationPageLocators.ADMINGROUP_TAB).click()
    def verify_show_all_admin_group_tab(self):
        self.find_element(*AdminGroupLocators.SHOW_ALL_ADMIN_GROUP_TAB)
    def verify_add_a_new_group_tab(self):
        self.find_element(*AdminGroupLocators.ADD_A_NEW_GROUP_TAB)
    def verify_show_entries_dropdown(self):
        self.find_element(*AdminGroupLocators.SHOW_ENTRIES_DROPDOWN)
    def verify_edit_admin_group_btn(self):
        self.find_element(*AdminGroupLocators.ACTION_EDIT_BUTTON)
    def click_edit_admin_group_btn(self):
        self.find_element(*AdminGroupLocators.ACTION_EDIT_BUTTON).click()
    def verify_edit_admin_page(self):
        self.find_element(*AdminGroupLocators.ADMIN_INFORMATION_BANNER)
        self.find_element(*AdminGroupLocators.ADMIN_DETAILED_INFO_BANNER)
    def edit_admin_info(self,username,email,phone,address):
        config.test_data['ADMIN_GROUP_PAGE'][0]['USERNAME'] = username
        self.find_element(*AdminGroupLocators.USERNAME_TEXTBOX).clear()
        self.find_element(*AdminGroupLocators.USERNAME_TEXTBOX).send_keys(username)
        config.test_data['ADMIN_GROUP_PAGE'][0]['USERNAME'] = username
        self.find_element(*AdminGroupLocators.EMAIL_TEXTBOX).clear()
        self.find_element(*AdminGroupLocators.EMAIL_TEXTBOX).send_keys(email)
        config.test_data['ADMIN_GROUP_PAGE'][0]['EMAIL'] = email
        self.find_element(*AdminGroupLocators.PHONE_TEXTBOX).clear()
        self.find_element(*AdminGroupLocators.PHONE_TEXTBOX).send_keys(phone)
        config.test_data['ADMIN_GROUP_PAGE'][0]['PHONE'] = phone
        self.find_element(*AdminGroupLocators.ADDRESS_TEXTBOX).clear()
        self.find_element(*AdminGroupLocators.ADDRESS_TEXTBOX).send_keys(address)
        config.test_data['ADMIN_GROUP_PAGE'][0]['ADDRESS'] = address
    def click_submit_admin_group_edits(self):
        self.find_element(*AdminGroupLocators.SUBMIT_BUTTON).click()
        time.sleep(5)
    def verify_edit_changes(self):
        s = config.test_data['ADMIN_GROUP_PAGE'][0]['EMAIL']
        EMAIL = (By.XPATH, "//*[contains(text()," + "'%s')]" % s)
        self.find_element(*EMAIL)

        s = config.test_data['ADMIN_GROUP_PAGE'][0]['USERNAME']
        USER_FIRST = (By.XPATH, "//*[contains(text()," + "'%s')]" %s)
        self.find_element(*USER_FIRST)

        s= config.test_data['ADMIN_GROUP_PAGE'][0]['PHONE']
        PHONE_FIRST = (By.XPATH, "//*[contains(text()," + "'%s')]" %s)
        self.find_element(*PHONE_FIRST)

        s = config.test_data ['ADMIN_GROUP_PAGE'][0]['ADDRESS']
        ADDRESS_FIRST = (By.XPATH, "//*[contains(text()," + "'%s')]" %s)
        self.find_element(*ADDRESS_FIRST)
    def click_add_a_new_group_tab(self):
        self.find_element(*AdminGroupLocators.ADD_A_NEW_GROUP_TAB).click()
    def add_a_new_group_info(self,username,email,phone,address):
        self.find_element(*AdminGroupLocators.USERNAME_TEXTBOX).clear()
        self.find_element(*AdminGroupLocators.USERNAME_TEXTBOX).send_keys(username)
        config.test_data['ADMIN_GROUP_PAGE'][0]['USERNAME'] = username
        self.find_element(*AdminGroupLocators.EMAIL_TEXTBOX).clear()
        self.find_element(*AdminGroupLocators.EMAIL_TEXTBOX).send_keys(email)
        config.test_data['ADMIN_GROUP_PAGE'][0]['EMAIL'] = email
        self.find_element(*AdminGroupLocators.PHONE_TEXTBOX).clear()
        self.find_element(*AdminGroupLocators.PHONE_TEXTBOX).send_keys(phone)
        config.test_data['ADMIN_GROUP_PAGE'][0]['PHONE'] = phone
        self.find_element(*AdminGroupLocators.ADDRESS_TEXTBOX).clear()
        self.find_element(*AdminGroupLocators.ADDRESS_TEXTBOX).send_keys(address)
        config.test_data['ADMIN_GROUP_PAGE'][0]['ADDRESS'] = address
    def change_status_pointer(self):
        self.find_element(*AdminGroupLocators.ACTIVE_POINTER).click()
    def click_view_admin_button(self):
        self.find_element(*AdminGroupLocators.SHOW_ADMIN).click()
    def verify_add_admin_elem(self):
        self.find_element(*AdminGroupLocators.USERNAME_ADD)
    def click_add_admin_elem(self):
        self.find_element(*AdminGroupLocators.ADD_ADMIN_TO_GROUP).click()
    def check_addmin_list(self):
        s = self.find_element(*AdminGroupLocators.ADDED_ADMIN_NAME).text
        config.test_data['ADMIN_GROUP_PAGE'][0]['CHECKADMIN'] = s
        self.find_element(*AdminGroupLocators.CHECK_ADMIN).click()
    def verify_added_admin(self):
        s = config.test_data['ADMIN_GROUP_PAGE'][0]['CHECKADMIN']
        FIND_ADMIN = (By.XPATH,"//*[contains(text()," + "'%s')]" %s)
        self.find_element(*FIND_ADMIN)










