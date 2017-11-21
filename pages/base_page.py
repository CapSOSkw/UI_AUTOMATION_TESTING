from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import Page
from locators.locators import *
import time
import random
from selenium.webdriver.support.ui import Select
import config

class BasePage(Page):
    def __init__(self, context):
        Page.__init__(self, context)

    def wait_time(self):
        time.sleep(5)

    def click_base_navigation_tab(self):
        self.find_element(*NavigationPageLocators.BASE_TAB).click()

    def verify_base_elements_exist(self):
        self.find_element(*BasePageLocators.SHOW_ALL_BASES)
        self.find_element(*BasePageLocators.ADD_A_NEW_BASE)
        self.find_element(*BasePageLocators.TABLE_BASENAME)
        self.find_element(*BasePageLocators.TABLE_COMPANY)
        self.find_element(*BasePageLocators.SEARCHING_BOX)

    def click_table_status(self):
        self.find_element(*BasePageLocators.TABLE_STATUS).click()

    def click_table_base_name(self):
        self.find_element(*BasePageLocators.TABLE_BASENAME).click()

    def click_table_base_type(self):
        self.find_element(*BasePageLocators.TABLE_BASETYPE).click()

    def click_table_company(self):
        self.find_element(*BasePageLocators.TABLE_COMPANY).click()

    def click_table_fare_type(self):
        self.find_element(*BasePageLocators.TABLE_FARE_TYPE).click()

    def click_add_a_new_base(self):
        self.find_element(*BasePageLocators.ADD_A_NEW_BASE).click()

    def click_action_edit_1st_base(self):
        self.find_element(*BasePageLocators.ACTION_FOR_1ST_BASE).click()

    def verify_edit_base_page_elements(self):
        self.find_element(*BasePageLocators.EDIT_COMPANY_DROPDOWN)
        self.find_element(*BasePageLocators.EDIT_AETNA_INSURANCE_EXP_DATE)
        self.find_element(*BasePageLocators.EDIT_ADDRESS)
        self.find_element(*BasePageLocators.EDIT_ZIPCODE)
        self.find_element(*BasePageLocators.EDIT_AUTO_SELF_INSURED)
        self.find_element(*BasePageLocators.EDIT_VISIT_TYPE)

    def enter_company(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_COMPANY_DROPDOWN))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass


    def enter_basename(self,basename):
        config.test_data_kw['BASE_PAGE'][0]['BASE_NAME'] = basename
        self.find_element(*BasePageLocators.EDIT_BASENAME).send_keys(basename)

    def enter_basetype(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_BASETYPE_DROPDOWN))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_fare_type(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_FARE_TYPE))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_federal_tax_id(self, id):
        self.find_element(*BasePageLocators.EDIT_FEDERAL_TAX_ID).send_keys(id)

    def enter_address(self,address):
        self.find_element(*BasePageLocators.EDIT_ADDRESS).send_keys(address)

    def enter_state(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_STATE))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_city(self,city):
        self.find_element(*BasePageLocators.EDIT_CITY).send_keys(city)

    def enter_zipcode(self,code):
        self.find_element(*BasePageLocators.EDIT_ZIPCODE).send_keys(code)

    def enter_main_contact(self, contact):
        self.find_element(*BasePageLocators.EDIT_MAIN_CONTACT).send_keys(contact)

    def enter_business_phone(self, phone):
        self.find_element(*BasePageLocators.EDIT_BUSINESS_PHONE).send_keys(phone)

    def enter_business_fax(self,fax):
        self.find_element(*BasePageLocators.EDIT_BUSINESS_FAX).send_keys(fax)

    def click_tracking_mode_active(self):
        button = self.find_element(*BasePageLocators.TRACKING_MODE_ACTIVE)
        button.click()

    def click_status_active(self):
        self.find_element(*BasePageLocators.EDIT_STATUS_ACTIVE).click()

    def enter_base_TLC_license_number(self, number):
        self.find_element(*BasePageLocators.EDIT_BASE_TLC_LICENSE_NUMBER).send_keys(number)

    def enter_base_TLC_license_start_date(self,date):
        self.find_element(*BasePageLocators.EDIT_BASE_TLC_LICENSE_START_DATE).send_keys(date)

    def enter_base_TLC_license_exp_date(self,date):
        self.find_element(*BasePageLocators.EDIT_BASE_TLC_LICENSE_EXP_DATE).send_keys(date)

    def enter_automobile_liability_amount(self, value):
        self.find_element(*BasePageLocators.EDIT_AUTOMOBILE_LIABILITY_AMOUNT).send_keys(value)

    def enter_auto_operr_certi_holder(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_AUTO_OPERR_CERTIFICATE_HOLDER))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_auto_self_insured(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_AUTO_SELF_INSURED))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_auto_operr_additional_insured(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_AUTO_OPERR_ADDITIONAL_INSURED))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_auto_name_afford_coverage(self, name):
        self.find_element(*BasePageLocators.EDIT_AUTO_NAME_AFFORD_COVERAGE).send_keys(name)

    def enter_auto_liability_insure_start_date(self, date):
        self.find_element(*BasePageLocators.EDIT_AUTOMOBILE_INSURANCE_START_DATE).send_keys(date)

    def enter_auto_liability_insure_exp_date(self, date):
        self.find_element(*BasePageLocators.EDIT_AUTOMOBILE_INSURANCE_EXP_DATE).send_keys(date)

    def enter_general_liability_amount(self, value):
        self.find_element(*BasePageLocators.EDIT_GENERAL_LIABILITY_AMOUNT).send_keys(value)

    def enter_general_operr_certi_holder(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_GENERAL_OPERR_CERTIFICATE_HOLDER))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_general_self_insured(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_GENERAL_SELF_INSURED))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_general_operr_additional_insured(self):
        try:
            select = Select(self.find_element(*BasePageLocators.EDIT_GENERAL_OPERR_ADDITIONAL_INSURED))
            options = [o.text for o in select.options]
            option = random.choice(options[1:])
            select.select_by_visible_text(option)
        except:
            pass

    def enter_general_name_afford_coverage(self, name):
        self.find_element(*BasePageLocators.EDIT_GENERAL_NAME_AFFORD_COVERAGE).send_keys(name)

    def enter_general_liability_insure_start_date(self, date):
        self.find_element(*BasePageLocators.EDIT_GENERAL_INSURANCE_START_DATE).send_keys(date)

    def enter_general_liability_insure_exp_date(self, date):
        self.find_element(*BasePageLocators.EDIT_GENERAL_INSURANCE_EXP_DATE).send_keys(date)

    def enter_IRS_business_name(self, name):
        self.find_element(*BasePageLocators.EDIT_IRS_NAME).send_keys(name)

    def enter_TIN_EIN_SNN(self, value):
        self.find_element(*BasePageLocators.EDIT_TIN_EIN_SNN).send_keys(value)

    def enter_federal_id_w9_start_date(self, date):
        self.find_element(*BasePageLocators.EDIT_FEDERAL_W9_START_DATE).send_keys(date)

    def enter_federal_id_w9_exp_date(self, date):
        self.find_element(*BasePageLocators.EDIT_FEDERAL_W9_EXP_DATE).send_keys(date)

    def enter_worker_compensation_amount(self, value):
        self.find_element(*BasePageLocators.EDIT_WORKER_COMPENSATION_AMOUNT).send_keys(value)


    def enter_worker_compensation_start_date(self, date):
        self.find_element(*BasePageLocators.EDIT_WORKER_COMPENSATION_START_DATE).send_keys(date)

    def enter_worker_compensation_exp_date(self, date):
        self.find_element(*BasePageLocators.EDIT_WORKER_COMPENSATION_EXP_DATE).send_keys(date)


    def enter_training_attest_start_date(self,date):
        self.find_element(*BasePageLocators.EDIT_TRAINING_ATT_START_DATE).send_keys(date)

    def enter_training_attest_exp_date(self,date):
        self.find_element(*BasePageLocators.EDIT_TRAINING_ATT_EXP_DATE).send_keys(date)

    def enter_schedule_a_start_date(self,date):
        self.find_element(*BasePageLocators.EDIT_SCHEDULE_A_START_DATE).send_keys(date)

    def enter_schedule_a_exp_date(self,date):
        self.find_element(*BasePageLocators.EDIT_SCHEDULE_A_EXP_DATE).send_keys(date)

    def enter_schedule_b_start_date(self,date):
        self.find_element(*BasePageLocators.EDIT_SCHEDULE_B_START_DATE).send_keys(date)

    def enter_schedule_b_exp_date(self,date):
        self.find_element(*BasePageLocators.EDIT_SCHEDULE_B_EXP_DATE).send_keys(date)

    def enter_aetna_insure_start_date(self,date):
        self.find_element(*BasePageLocators.EDIT_AETNA_INSURANCE_START_DATE).send_keys(date)

    def enter_aetna_insure_exp_date(self,date):
        self.find_element(*BasePageLocators.EDIT_AETNA_INSURANCE_EXP_DATE).send_keys(date)

    def enter_insure_endorsement_start_date(self, date):
        self.find_element(*BasePageLocators.EDIT_INSURANCE_ENDORSEMENT_START_DATE).send_keys(date)

    def enter_insure_endorsement_exp_date(self, date):
        self.find_element(*BasePageLocators.EDIT_INSURANCE_ENDORSEMENT_EXP_DATE).send_keys(date)

    def enter_NYCT_start_date(self,date):
        self.find_element(*BasePageLocators.EDIT_NYCT_START_DATE).send_keys(date)

    def enter_NYCT_exp_date(self,date):
        self.find_element(*BasePageLocators.EDIT_NYCT_EXP_DATE).send_keys(date)

    def enter_service_agreement_start_date(self, date):
        self.find_element(*BasePageLocators.EDIT_SERVICE_AGREE_START_DATE).send_keys(date)

    def enter_service_agreement_exp_date(self, date):
        self.find_element(*BasePageLocators.EDIT_SERVICE_AGREE_EXP_DATE).send_keys(date)

    def enter_wellcare_start_date(self, date):
        self.find_element(*BasePageLocators.EDIT_WELLCARE_START_DATE).send_keys(date)

    def enter_wellcare_exp_date(self,date):
        self.find_element(*BasePageLocators.EDIT_WELLCARE_EXP_DATE).send_keys(date)

    def click_base_submit(self):
        self.find_element(*BasePageLocators.BASE_SUBMIT).click()

    def verify_new_base_exists(self):
        s = config.test_data_kw['BASE_PAGE'][0]['BASE_NAME']
        NEW_BASE = (By.XPATH, "//*[contains(text()," + "'%s')]" %s)
        self.find_element(*NEW_BASE)

    def click_action_button_for_1st_base(self):
        self.find_element(*BasePageLocators.ACTION_FOR_1ST_BASE).click()

    def clear_base_data(self):
        self.find_element(*BasePageLocators.EDIT_BASENAME).clear()
        self.find_element(*BasePageLocators.EDIT_BASETYPE_DROPDOWN)
        self.find_element(*BasePageLocators.EDIT_FEDERAL_TAX_ID).clear()
        self.find_element(*BasePageLocators.EDIT_ADDRESS).clear()
        self.find_element(*BasePageLocators.EDIT_CITY).clear()
        self.find_element(*BasePageLocators.EDIT_ZIPCODE).clear()
        self.find_element(*BasePageLocators.EDIT_MAIN_CONTACT).clear()
        self.find_element(*BasePageLocators.EDIT_BUSINESS_PHONE).clear()
        self.find_element(*BasePageLocators.EDIT_BUSINESS_FAX).clear()
        self.find_element(*BasePageLocators.EDIT_BASE_TLC_LICENSE_NUMBER).clear()
        self.find_element(*BasePageLocators.EDIT_BASE_TLC_LICENSE_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_BASE_TLC_LICENSE_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_AUTOMOBILE_LIABILITY_AMOUNT).clear()
        self.find_element(*BasePageLocators.EDIT_AUTO_NAME_AFFORD_COVERAGE).clear()
        self.find_element(*BasePageLocators.EDIT_AUTOMOBILE_INSURANCE_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_AUTOMOBILE_INSURANCE_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_GENERAL_LIABILITY_AMOUNT).clear()
        self.find_element(*BasePageLocators.EDIT_GENERAL_NAME_AFFORD_COVERAGE).clear()
        self.find_element(*BasePageLocators.EDIT_GENERAL_INSURANCE_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_GENERAL_INSURANCE_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_IRS_NAME).clear()
        self.find_element(*BasePageLocators.EDIT_TIN_EIN_SNN).clear()
        self.find_element(*BasePageLocators.EDIT_FEDERAL_W9_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_FEDERAL_W9_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_WORKER_COMPENSATION_AMOUNT).clear()
        self.find_element(*BasePageLocators.EDIT_WORKER_COMPENSATION_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_WORKER_COMPENSATION_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_TRAINING_ATT_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_TRAINING_ATT_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_SCHEDULE_A_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_SCHEDULE_A_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_SCHEDULE_B_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_SCHEDULE_B_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_AETNA_INSURANCE_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_AETNA_INSURANCE_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_INSURANCE_ENDORSEMENT_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_INSURANCE_ENDORSEMENT_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_NYCT_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_NYCT_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_SERVICE_AGREE_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_SERVICE_AGREE_EXP_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_WELLCARE_START_DATE).clear()
        self.find_element(*BasePageLocators.EDIT_WELLCARE_EXP_DATE).clear()