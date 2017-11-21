from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import config
import random, string
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page
from pages.inactive_drivers_page import InactiveDriverPage
from pages.company_page import CompanyPage

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@when('user clicks the add a new company button')
def step_impl(context):
    page = CompanyPage(context)
    page.click_add_a_new_company_button()
    pass

@then('user can add a new company')
def step_impl(context):
    page = CompanyPage(context)
    page.verify_add_company_elements_exist()
    pass

@then('user edits the company name')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_company_name('Company'+randomword(2))
    pass

@then('user edits the days in week')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_days_in_week()
    pass

@then('user edits the start worktime')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_start_worktime('08', '30')
    pass

@then('user edits the end worktime')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_end_worktime('20', '30')
    pass

@then('user edits the phone number')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_phone_number('1234567890')
    pass

@then('user edits the email')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_email(randomword(4))
    pass

@then('user edits the address')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_address(randomword(5))
    pass

@then('user edits the state')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_state()
    pass

@then('user edits the city')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_city('New York')
    pass

@then('user edits the zipcode')
def step_impl(context):
    page = CompanyPage(context)
    page.enter_zipcode('10086')
    pass

@then('user chooses active status')
def step_impl(context):
    page = CompanyPage(context)
    page.click_active()
    pass

@then('user clicks submit button on add a new company page')
def step_impl(context):
    page = CompanyPage(context)
    page.click_submit_btn()
    page.wait_time()
    pass

@then('a new company is added')
def step_impl(context):
    page = CompanyPage(context)
    page.verify_new_company_added()
    page.wait_time()
    pass