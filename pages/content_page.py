from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import Page
from locators.locators import *
import time
import random, string
from selenium.webdriver.support.ui import Select
import config

class ContentPage(Page):
    def __init__(self, context):
        Page.__init__(self, context)

    def wait_time(self):
        time.sleep(5)

    def click_content_navigation_tab(self):
        self.find_element(*NavigationPageLocators.CONTENT_TAB).click()

    def verify_content_elements_exist(self):
        self.find_element(*ContentPageLocators.SHOW_ALL_CONTENT)
        self.find_element(*ContentPageLocators.ADD_A_NEW_CONTENT)
        self.find_element(*ContentPageLocators.TABLE_BASENAME)
        self.find_element(*ContentPageLocators.TABLE_STATUS)
        self.find_element(*ContentPageLocators.TABLE_DATE)
        self.find_element(*ContentPageLocators.TABLE_TITLE)
        self.find_element(*ContentPageLocators.ACTION_EDIT_FOR_1ST_CONTENT)

    def click_add_a_new_content(self):
        self.find_element(*ContentPageLocators.ADD_A_NEW_CONTENT).click()

    def enter_base(self):
        try:
            select = Select(self.find_element(*ContentPageLocators.EDIT_BASE))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_title(self, title):
        config.test_data_kw['CONTENT_PAGE'][0]['TITLE'] = title
        self.find_element(*ContentPageLocators.EDIT_TITLE).send_keys(title)

    def enter_description(self, des):
        el = self.find_element(*ContentPageLocators.EDIT_DESCRIPTION).click()
        time.sleep(5)
        try:
            self.find_element(*ContentPageLocators.EDIT_DESCRIPTION_INPUT).send_keys(des)
        except:
            pass

    def enter_page_title(self, page_title):
        self.find_element(*ContentPageLocators.EDIT_PAGE_TITLE).send_keys(page_title)

    def enter_page_keywords(self, keyword):
        self.find_element(*ContentPageLocators.EDIT_PAGE_KEYWORDS).send_keys(keyword)

    def click_status_active(self):
        self.find_element(*ContentPageLocators.EDIT_STATUS_ACTIVE).click()

    def verify_edit_elements_exist(self):
        self.find_element(*ContentPageLocators.EDIT_BASE)
        self.find_element(*ContentPageLocators.EDIT_TITLE)
        self.find_element(*ContentPageLocators.EDIT_PAGE_TITLE)
        self.find_element(*ContentPageLocators.EDIT_STATUS_ACTIVE)

    def click_content_submit_button(self):
        self.find_element(*ContentPageLocators.SUBMIT_BUTTON).click()

    def click_action_for_1st_content(self):
        self.find_element(*ContentPageLocators.ACTION_EDIT_FOR_1ST_CONTENT).click()

    def clear_content_info(self):
        self.find_element(*ContentPageLocators.EDIT_TITLE).clear()
        self.find_element(*ContentPageLocators.EDIT_PAGE_TITLE).clear()
        self.find_element(*ContentPageLocators.EDIT_PAGE_KEYWORDS).clear()

    def verify_new_content_exists(self):
        s = config.test_data_kw['CONTENT_PAGE'][0]['TITLE']
        NEW_CONTENT = (By.XPATH, "//*[contains(text()," + "'%s')]" %s)
        self.find_element(*NEW_CONTENT)
