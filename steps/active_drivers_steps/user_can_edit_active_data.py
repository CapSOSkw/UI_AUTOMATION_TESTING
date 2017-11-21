from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page
from pages.inactive_drivers_page import InactiveDriverPage
from pages.active_drivers_page import ActiveDriverPage

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@when('user clicks the active username button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_username()
    pass

@then('user can see active username-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active action edit button for the first username')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_action_edit_1st_user()
    pass

@then('user can see all information of this active user')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@then('user clears the active driver information')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.clear_active_information()
    pass

@then('user edits the active driver first name')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_firstname('A'+randomword(3))
    pass

@then('user edits the active driver last name')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_lastname('A'+randomword(3))
    pass

@then('user edits the active driver username')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_username('A123'+randomword(6))
    pass

@then('user edits the active driver email')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_email('A'+randomword(2))
    pass

@then('user edits the active driver password')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_password('123456789')
    pass

@then('user edits the active driver phone number')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_phone_number('1234567890')
    pass

@then('user edits the active driver date of birth')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_birthday("01/01/1990")
    pass

@then('user edits the active driver gender')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_gender()
    pass

@then('user edits the active driver country of origin')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_country()
    pass

@then('user edits the active driver driving experience')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_driving_exp('9')
    pass

@then('user edits the active driver type')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_driver_type()
    pass

@then('user edits the active driver affiliated company name')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_affiliated_company()
    pass

@then('user edits the active driver affiliated based name')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_affiliated_base()
    pass

@then('user edits the active driver license number')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_driver_license_number('888886666')
    pass

@then('user edits the active driver license class')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_driver_license_class('C')
    pass

@then('user edits the active driver license state')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_driver_license_state()
    pass

@then('user edits the active driver license start date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_driver_license_start_date("01/01/2010")
    pass

@then('user edits the active driver license expire date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_active_driver_license_exp_date("01/01/2018")
    pass

@then('user edits the active driver TLC FHV license number')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_TLC_FHV_number("666666")
    pass

@then('user edits the active driver TLC FHV license start date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_TLC_FHV_start_date("01/01/2011")
    pass

@then('user edits the active driver TLC FHV license expire date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_TLC_FHV_exp_date("01/01/2018")
    pass

@then('user edits the active driver background check start date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_background_check_start_date("01/01/2016")
    pass

@then('user edits the active driver background check expire date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_background_check_exp_date("01/01/2018")
    pass

@then('user edits the active driver driving record start date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_driving_record_start_date("01/01/2017")
    pass

@then('user edits the active driver driving record expire date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_driving_record_exp_date("01/01/2018")
    pass

@then('user edits the active driver drug screen start date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_drug_screen_start_date("01/01/2015")
    pass

@then('user edits the active driver drug screen expire date')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_drug_screen_exp_date("01/01/2018")
    pass

@then('user edits the active driver vehicle info')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_vehicle_info()
    pass

@then('user edits the active cross county')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_cross_county_both()
    pass

@then('user clicks active driver page submit button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_edit_submit_btn()
    page.wait_time()
    pass

@then('an active driver is changed')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_driver_tab()
    page.wait_time()
    page.click_active_username()
    page.wait_time()
    page.verify_new_username_exist()
    page.wait_time()
    pass