from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page
from pages.inactive_drivers_page import InactiveDriverPage
from pages.base_page import BasePage

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@when('user clicks add a new base')
def step_impl(context):
    page = BasePage(context)
    page.click_add_a_new_base()
    pass

@then('user can add a new base')
def step_impl(context):
    page = BasePage(context)
    page.verify_edit_base_page_elements()
    pass

@then('user edits the base company')
def step_impl(context):
    page = BasePage(context)
    page.enter_company()
    pass

@then('user edits the base base name')
def step_impl(context):
    page = BasePage(context)
    page.enter_basename('Base'+randomword(2))
    pass

@then('user edits the base base type')
def step_impl(context):
    page = BasePage(context)
    page.enter_basetype()
    pass

@then('user edits the base fare type')
def step_impl(context):
    page = BasePage(context)
    page.enter_fare_type()
    pass

@then('user edits the base federal tax id')
def step_impl(context):
    page = BasePage(context)
    page.enter_federal_tax_id('88888888')
    pass

@then('user edits the base address')
def step_impl(context):
    page = BasePage(context)
    page.enter_address('10086 '+randomword(4)+' St.')
    pass

@then('user edits the base state')
def step_impl(context):
    page = BasePage(context)
    page.enter_state()
    pass

@then('user edits the base city')
def step_impl(context):
    page = BasePage(context)
    page.enter_city('NYC')
    pass

@then('user edits the base zipcode')
def step_impl(context):
    page = BasePage(context)
    page.enter_zipcode('10086')
    pass

@then('user edits the base main contact')
def step_impl(context):
    page = BasePage(context)
    page.enter_main_contact('John Smith')
    pass

@then('user edits the base business phone')
def step_impl(context):
    page = BasePage(context)
    page.enter_business_phone('1234567890')
    pass

@then('user edits the base business fax')
def step_impl(context):
    page = BasePage(context)
    page.enter_business_fax('1234567890')
    page.wait_time()
    pass

@then('user clicks the base tracking mode active button')
def step_impl(context):
    page = BasePage(context)
    page.click_tracking_mode_active()
    pass

@then('user clicks the base status active button')
def step_impl(context):
    page = BasePage(context)
    page.click_status_active()
    pass

@then('user edits the base TLC license number')
def step_impl(context):
    page = BasePage(context)
    page.enter_base_TLC_license_number('B10086')
    pass

@then('user edits the base TLC license start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_base_TLC_license_start_date('01/01/2016')
    pass

@then('user edits the base TLC license exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_base_TLC_license_exp_date('01/01/2018')
    pass

@then('user edits the base auto liability amount')
def step_impl(context):
    page = BasePage(context)
    page.enter_automobile_liability_amount('1000000')
    pass

@then('user edits the base auto operr certificate holder')
def step_impl(context):
    page = BasePage(context)
    page.enter_auto_operr_certi_holder()
    pass

@then('user edits the base auto self insured')
def step_impl(context):
    page = BasePage(context)
    page.enter_auto_operr_additional_insured()
    pass

@then('user edits the base auto operr additional insured')
def step_impl(context):
    page = BasePage(context)
    page.enter_auto_operr_additional_insured()
    pass

@then('user edits the base auto name afford coverage')
def step_impl(context):
    page = BasePage(context)
    page.enter_auto_name_afford_coverage('AAA')
    pass

@then('user edits the base auto insurance start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_auto_liability_insure_start_date('01/01/2016')
    pass

@then('user edits the base auto insurance exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_auto_liability_insure_exp_date('01/01/2018')
    pass

@then('user edits the base general liability amount')
def step_impl(context):
    page = BasePage(context)
    page.enter_general_liability_amount('100000')
    pass

@then('user edits the base general operr certificate holder')
def step_impl(context):
    page = BasePage(context)
    page.enter_general_operr_certi_holder()
    pass

@then('user edits the base general self insured')
def step_impl(context):
    page = BasePage(context)
    page.enter_general_self_insured()
    pass

@then('user edits the base general operr additional insured')
def step_impl(context):
    page = BasePage(context)
    page.enter_general_operr_additional_insured()
    pass

@then('user edits the base general name afford coverage')
def step_impl(context):
    page = BasePage(context)
    page.enter_general_name_afford_coverage('AAA')
    pass

@then('user edits the base general insurance start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_general_liability_insure_start_date('01/01/2016')
    pass

@then('user edits the base general insurancce exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_general_liability_insure_exp_date('01/01/2018')
    pass

@then('user edits the base IRS business name')
def step_impl(context):
    page = BasePage(context)
    page.enter_IRS_business_name('Base'+randomword(8))
    pass

@then('user edits the base TIN EIN SNN')
def step_impl(context):
    page = BasePage(context)
    page.enter_TIN_EIN_SNN('666666666')
    pass

@then('user edits the base federal id w9 start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_federal_id_w9_start_date('01/01/2016')
    pass

@then('user edits the base federal id w9 exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_federal_id_w9_exp_date('01/01/2018')
    pass

@then('user edits the base worker compensation amount')
def step_impl(context):
    page = BasePage(context)
    page.enter_worker_compensation_amount('100000')
    pass

@then('user edits the base worker compensation start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_worker_compensation_start_date('01/01/2017')
    pass

@then('user edits the base worker compensation exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_worker_compensation_exp_date('01/01/2019')
    pass

@then('user edits the base training attest start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_training_attest_start_date('01/01/2017')
    pass

@then('user edits the base training attest exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_training_attest_exp_date('06/01/2017')
    pass

@then('user edits the base schedule a start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_schedule_a_start_date('01/01/2017')
    pass

@then('user edits the base schedule a exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_schedule_a_exp_date('01/01/2018')
    pass

@then('user edits the base schedule b start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_schedule_b_start_date('02/02/2017')
    pass

@then('user edits the base schedule b exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_schedule_b_exp_date('02/02/2018')
    pass

@then('user edits the base aetna start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_aetna_insure_start_date('01/01/2016')
    pass

@then('user edits the base aetna exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_aetna_insure_exp_date('01/01/2018')
    pass

@then('user edits the base insurance endorsement start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_insure_endorsement_start_date('01/01/2016')
    pass

@then('user edits the base insurance endorsement exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_insure_endorsement_exp_date('01/01/2018')
    pass

@then('user edits the base NYCT start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_NYCT_start_date('01/01/2017')
    pass

@then('user edits the base NYCT exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_NYCT_exp_date('01/01/2018')
    pass

@then('user edits the base service agreement start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_service_agreement_start_date('01/01/2017')
    pass

@then('user edits the base service agreement exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_service_agreement_exp_date('01/01/2018')
    pass

@then('user edits the base wellcare start date')
def step_impl(context):
    page = BasePage(context)
    page.enter_wellcare_start_date('01/01/2017')
    pass

@then('user edits the base wellcare exp date')
def step_impl(context):
    page = BasePage(context)
    page.enter_wellcare_exp_date('01/01/2018')
    pass

@then('user clicks the base submit button')
def step_impl(context):
    page = BasePage(context)
    page.click_base_submit()
    pass

@then('a new base is added')
def step_impl(context):
    page = BasePage(context)
    page.wait_time()
    page.click_table_base_name()
    page.verify_new_base_exists()
    pass